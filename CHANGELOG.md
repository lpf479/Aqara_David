# 更新日志

## 版本 26.2.24.2 (David's Enhanced Version)

### 新增功能
- ✨ 新增 `button.py` - 支持按钮设备
- ✨ 新增 `number.py` - 支持数字输入设备
- ✨ 新增 `select.py` - 支持选择器设备

### 增强优化
- 📦 更新 `aiot_mapping.py` - 扩展设备映射支持（156KB vs 原版105KB）
- 🔧 优化设备兼容性和稳定性

### 文件结构
```
custom_components/aqara_bridge/
├── __init__.py           # 核心初始化
├── manifest.json         # 集成清单
├── config_flow.py        # 配置流程
├── 3rd_libs/            # 第三方库（rocketmq）
├── core/                # 核心模块
│   ├── aiot_cloud.py    # 云端API
│   ├── aiot_manager.py  # 设备管理
│   ├── aiot_mapping.py  # 设备映射（增强版）
│   ├── const.py         # 常量定义
│   └── utils.py         # 工具函数
├── translations/        # 多语言支持
│   ├── en.json
│   └── zh-Hans.json
└── 设备类型模块:
    ├── light.py         # 灯光
    ├── switch.py        # 开关
    ├── sensor.py        # 传感器
    ├── binary_sensor.py # 二元传感器
    ├── climate.py       # 空调/温控
    ├── cover.py         # 窗帘
    ├── remote.py        # 遥控器
    ├── event.py         # 事件
    ├── air_quality.py   # 空气质量
    ├── button.py        # 按钮（新增）
    ├── number.py        # 数字输入（新增）
    └── select.py        # 选择器（新增）
```

### 基于原版
本版本基于 [bernard3378/AqaraBridge](https://github.com/bernard3378/AqaraBridge) 开发

---

## 原版更新历史

### V2.1.2
- 优化初始化向导提示
- 优化设备初始化流程
- 优化人体场景传感器FP2状态管理
- 优化人体存在传感器FP1/FP1E移动事件

### V2.1.1
- 修复窗帘位置同步不及时问题
- 修改将被HA弃用的函数
- 完善arm64架构rocketmq支持
- 优化初始化时可能创建无法管理的实体的问题
- 按钮button改为event类

### V2.1.0
- 重写空调控制器类
- 修复rocketmq启动时阻塞HA初始化问题
- 修复了调用某些HA已废弃/将要废弃常量问题
- 修复light设备类颜色映射错误
