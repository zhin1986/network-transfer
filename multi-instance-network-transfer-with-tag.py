import requests

# 在脚本内部设置参数
API_KEY = ' '
tagLabel = ' '

# 获取标签下的所有实例 ID
def get_tagged_instance_ids():
    url = f'https://api.linode.com/v4/tags/{tagLabel}?page=1&page_size=100'
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        instance_ids = []
        for item in data.get('data', []):
            if 'data' in item and 'id' in item['data']:
                instance_ids.append(item['data']['id'])
            else:
                print(f"Item does not have the required keys: {item}")
        return instance_ids
    else:
        print(f"Failed to retrieve tagged instances: {response.status_code}")
        print(f"Reason: {response.reason}")
        return []

# 获取实例的流量使用情况并计算总和
def get_total_used_gb(instance_ids):
    total_used_gb = 0
    for instance_id in instance_ids:
        url = f'https://api.linode.com/v4/linode/instances/{instance_id}/transfer'
        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {API_KEY}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            used_gb = data["used"] / (1024 ** 3)  # 将字节转换为GB
            print(f"Instance {instance_id} Used: {used_gb:.2f} GB")
            total_used_gb += used_gb
        else:
            print(f"Failed to retrieve data for instance {instance_id}: {response.status_code}")
            print(f"Reason: {response.reason}")
    return total_used_gb

# 主函数
def main():
    instance_ids = get_tagged_instance_ids()
    if instance_ids:
        total_used_gb = get_total_used_gb(instance_ids)
        print(f"Total Used: {total_used_gb:.2f} GB")

if __name__ == "__main__":
    main()
