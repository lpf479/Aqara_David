# Aqara_David - Aqara Bridge for Home Assistant

[![version](https://img.shields.io/badge/version-26.2.24.2-blue.svg)](https://github.com/lpf479/Aqara_David/releases)
[![hacs](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

基于Aqara开放平台，通过云端API进行设备控制以及订阅。

**本版本特点**:
- 🚀 在原版基础上增强，支持更多设备类型
- 🔒 已清理所有敏感信息，可安全分享
- 📚 完整的中文文档和使用指南
- ✨ 新增Button、Number、Select设备支持
- 🛠️ 扩展的设备映射（156KB vs 原版105KB）

## 版本信息

**当前版本**: 26.2.24.2

**新增设备支持**:
- Button 按钮设备 (button.py)
- Number 数字输入设备 (number.py)
- Select 选择器设备 (select.py)

**核心功能**:
- ✅ 支持Aqara云端设备控制
- ✅ 实时消息推送订阅
- ✅ 多种设备类型支持（灯光、开关、传感器、空调、窗帘等）
- ✅ 支持中国、美国、韩国、俄罗斯、德国服务器

## 安装要求

### 1. 申请Aqara开发者账号

**必须先申请Aqara IoT开发者账号**: [Aqara IoT Cloud](https://developer.aqara.com/register)

**申请流程**:

1. **注册账号**: 访问 [注册页面](https://developer.aqara.com/register)
2. **个人认证**: 申请通过后选择个人认证，输入姓名和身份证号进行开发者认证
3. **配置消息推送**:
   - 进入项目管理 → 详情 → 消息推送 → 编辑
   - 选择：中国服务、MQ消息推送、消息密钥（默认应该只有一个）、全订阅
   - 点击保存
4. **获取密钥**:
   - 返回概况页面
   - 点击"Appid&密钥"展开
   - 找到中国服务，记录以下三个参数：
     - `appId`
     - `appKey`（需要点击小眼睛查看）
     - `keyId`

### 2. 系统要求

- Home Assistant 2024.1.0 或更高版本
- Python 3.11 或更高版本
- 支持架构: x86_64, arm64

## 快速开始

### 三步完成安装

1. **通过HACS安装** → 添加自定义仓库并安装
2. **申请开发者账号** → 获取appId、appKey、keyId
3. **配置集成** → 在HA中添加集成并输入凭证

详细步骤请参考下方的安装方法和配置说明。

## 安装方法

### 方法一: HACS安装（推荐）

1. 确保已安装 [HACS](https://hacs.xyz/)
2. 在HACS中添加自定义存储库:
   - 点击 HACS → Integrations → 右上角三个点 → Custom repositories
   - 添加此仓库URL
   - 类别选择: Integration
3. 搜索 "Aqara Bridge" 并安装
4. 重启 Home Assistant

### 方法二: 手动安装

1. 下载此仓库
2. 将 `custom_components/aqara_bridge` 文件夹复制到你的 Home Assistant 配置目录下的 `custom_components/` 文件夹中
3. 重启 Home Assistant

## 配置说明

### 首次配置

1. 进入 Home Assistant → 设置 → 设备与服务 → 添加集成
2. 搜索 "Aqara Bridge"
3. 输入以下信息:
   - **账号**: 你的Aqara账号（手机号或邮箱）
   - **国家代码**: 选择你的服务器区域（中国选CN）
   - **App ID**: 从开发者平台获取的appId
   - **App Key**: 从开发者平台获取的appKey
   - **Key ID**: 从开发者平台获取的keyId
4. 点击提交，等待获取授权码
5. 输入收到的授权码完成配置

### 重新授权

如果token过期，可以通过以下方式重新授权:

1. 进入集成设置 → 配置
2. 输入账号和国家代码
3. 获取新的授权码并输入

## 支持的设备类型

- **灯光** (Light): 智能灯泡、灯带驱动器等
- **开关** (Switch): 墙壁开关、无线开关、插座等
- **传感器** (Sensor): 温湿度、门窗、人体等传感器
- **二元传感器** (Binary Sensor): 门窗状态、人体检测等
- **气候** (Climate): 空调控制器、温控器等
- **窗帘** (Cover): 智能窗帘、卷帘等
- **遥控器** (Remote): 万能遥控器等
- **事件** (Event): 按钮事件、手势识别等
- **空气质量** (Air Quality): 空气质量监测器
- **按钮** (Button): 场景按钮等
- **数字输入** (Number): 数值调节设备
- **选择器** (Select): 模式选择设备

## 调试说明

如需查看详细日志，可在 `configuration.yaml` 中添加:

```yaml
logger:
  default: warning
  logs:
    custom_components.aqara_bridge: info
```

重启后可在日志中查看消息推送和设备状态更新情况。

## 常见问题

### Q: 提示"此集成不支持通过UI配置"

A: 这通常是因为rocketmq链接库不存在。当前版本支持x86_64和arm64架构，如果你使用其他架构，请提交Issue。

### Q: 设备无法控制或状态不更新

A: 
1. 检查token是否过期，尝试重新授权
2. 确认消息推送配置正确（全订阅）
3. 查看日志是否有错误信息

### Q: 如何查看支持的设备列表

A: 查看 `core/aiot_mapping.py` 文件，其中包含所有支持的设备型号和功能映射。

## 安全说明

### ✅ 本项目安全性

本项目已经过完整的安全检查：
- ✅ **无硬编码密钥**: 所有代码文件不包含任何API密钥或token
- ✅ **无IP地址**: 不包含任何硬编码的IP地址或服务器地址
- ✅ **无个人信息**: 不包含任何个人账号、密码等敏感信息
- ✅ **已清理缓存**: 所有`__pycache__`和`.pyc`文件已清理

### ⚠️ 使用注意事项

**隐私保护**:
- 🔐 不要在公开场合分享你的appId、appKey、keyId
- 🔐 不要提交包含个人凭证的配置文件到GitHub
- 🔐 定期在Aqara开发者平台更换密钥
- 🔐 使用HTTPS访问Home Assistant

**使用限制**:
- ⚡ Aqara云端API有调用频率限制
- ⚡ 建议不要频繁刷新设备状态
- ⚡ 依赖消息推送而非轮询获取状态更新

## 贡献与支持

本项目基于 [bernard3378/AqaraBridge](https://github.com/bernard3378/AqaraBridge) 开发。

如遇到问题或有功能建议，欢迎提交Issue。

## 项目文件结构

```
custom_components/aqara_bridge/
├── __init__.py              # 核心初始化模块
├── manifest.json            # 集成清单文件
├── config_flow.py           # 配置流程处理
├── 3rd_libs/               # 第三方库
│   ├── arm64/              # ARM64架构RocketMQ库
│   └── x86_64/             # x86_64架构RocketMQ库
├── core/                   # 核心功能模块
│   ├── aiot_cloud.py       # Aqara云端API接口
│   ├── aiot_manager.py     # 设备管理器
│   ├── aiot_mapping.py     # 设备映射配置（增强版156KB）
│   ├── const.py            # 常量定义
│   └── utils.py            # 工具函数
├── translations/           # 多语言支持
│   ├── en.json             # 英文翻译
│   └── zh-Hans.json        # 简体中文翻译
└── 设备类型模块/
    ├── light.py            # 灯光设备
    ├── switch.py           # 开关设备
    ├── sensor.py           # 传感器
    ├── binary_sensor.py    # 二元传感器
    ├── climate.py          # 空调/温控设备
    ├── cover.py            # 窗帘设备
    ├── remote.py           # 遥控器
    ├── event.py            # 事件设备
    ├── air_quality.py      # 空气质量监测
    ├── button.py           # 按钮设备（新增）
    ├── number.py           # 数字输入设备（新增）
    └── select.py           # 选择器设备（新增）
```

## 相关文档

- 📖 [安装指南](INSTALL.md) - 详细的安装步骤
- 📖 [使用指南](USAGE.md) - 完整的使用教程和自动化示例
- 📖 [更新日志](CHANGELOG.md) - 版本更新记录
- 📖 [项目信息](PROJECT_INFO.md) - 技术栈和项目详情
- 📖 [发布清单](RELEASE_CHECKLIST.md) - GitHub发布检查清单

## 许可证

MIT License - 本项目遵循MIT开源许可证，允许自由使用、修改和分发。

## 致谢

- 原作者: [@bernard3378](https://github.com/bernard3378)
- 贡献者: [@angeljanne](https://github.com/angeljanne), [@meishild](https://github.com/meishild)
- Aqara开放平台: [https://developer.aqara.com](https://developer.aqara.com)
