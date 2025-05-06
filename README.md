# network-transfer
## 1. 获取标签下的实例 ID：
+ 调用 get_tagged_instance_ids 函数，根据标签 "ZX-TEST" 获取所有实例 ID。
+ 构建 API URL 并发送请求，检查响应状态码。
+ 如果请求成功，解析响应数据，提取每个实例的 ID 并存储在列表中返回。
## 2. 获取实例的流量使用情况并计算总和：
+ 调用 get_total_used_gb 函数，传入实例 ID 列表。
+ 遍历每个实例 ID，构建对应的 API URL 并发送请求。
+ 如果请求成功，将流量使用量从字节转换为 GB，打印该实例的使用量，并将其添加到总流量中。
+ 如果请求失败，输出相应的错误信息。
## 3. 主函数：
调用 get_tagged_instance_ids 获取实例 ID 列表。
如果成功获取实例 ID 列表，调用 get_total_used_gb 获取总流量使用量并打印。
