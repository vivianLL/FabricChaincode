# FabricChaincodeAndDeployment（4Org）
基于Fabric编写的一个多机多组织实现投标中标记账功能的链码
具体功能：
发布合约-招标
响应合约-投标
成交合约-中标
关闭合约
查询合约（查询分类：历史合约、最新合约；权限设置：招标人可查全部，投标人只能查自己）
（基本验证：调用接口的用户代码和功能对应的用户代码是否相同、验证合约状态和调用功能是否逻辑一致，验证参数是否正确等）

具体开发部署过程和启动步骤：
fabirc链码开发及在开发模式下的调试https://blog.csdn.net/vivian_ll/article/details/80339943
多机上部署多个组织（4org）的fabric网络https://blog.csdn.net/vivian_ll/article/details/80597091
多机上启动多组织（4org）的fabric网络https://blog.csdn.net/vivian_ll/article/details/80597668
