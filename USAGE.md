# 使用指南

## 配置前准备

### 1. 获取Aqara开发者凭证

访问 [Aqara开发者平台](https://developer.aqara.com) 并登录你的账号。

**获取步骤**:
1. 进入"项目管理"
2. 选择你的项目（或使用默认的DEMO应用）
3. 点击"概况"
4. 展开"Appid&密钥"
5. 选择"中国服务"（或你所在的区域）
6. 记录以下信息：
   - **App ID**: 应用ID
   - **App Key**: 应用密钥（点击眼睛图标查看）
   - **Key ID**: 密钥ID

### 2. 配置消息推送

**重要**: 必须配置消息推送才能接收设备状态更新！

1. 进入"项目管理" → "详情"
2. 点击"消息推送" → "编辑"
3. 配置以下选项：
   - ✅ 服务器: 选择"中国服务"（或你的区域）
   - ✅ 推送方式: 选择"MQ消息推送"
   - ✅ 消息密钥: 选择默认密钥
   - ✅ 订阅类型: 选择"全订阅"
4. 点击"保存"

## Home Assistant配置

### 首次添加集成

1. **进入集成页面**
   - 设置 → 设备与服务 → 添加集成

2. **搜索并选择**
   - 搜索"Aqara Bridge"
   - 点击选择

3. **输入基本信息**
   - **账号**: 你的Aqara账号（手机号或邮箱）
   - **国家代码**: 
     - CN - 中国
     - USA - 美国
     - KR - 韩国
     - RU - 俄罗斯
     - GER - 德国
   - **App ID**: 从开发者平台复制
   - **App Key**: 从开发者平台复制
   - **Key ID**: 从开发者平台复制

4. **获取授权码**
   - 点击"提交"后，系统会发送授权码到你的Aqara账号
   - 检查手机短信或邮箱

5. **输入授权码**
   - 在弹出的窗口中输入收到的授权码
   - 点击"提交"完成配置

### 重新授权（Token过期时）

如果出现设备无法控制或状态不更新的情况，可能是token过期：

1. 进入集成设置
   - 设置 → 设备与服务 → Aqara Bridge
   - 点击"配置"

2. 重新输入信息
   - 输入账号和国家代码
   - 获取新的授权码
   - 输入授权码完成重新授权

## 设备管理

### 查看设备

配置完成后，所有绑定到你Aqara账号的设备会自动添加到Home Assistant。

**查看方式**:
- 设置 → 设备与服务 → Aqara Bridge → 设备

### 设备类型

支持的设备类型包括：

| 类型 | 说明 | 示例 |
|------|------|------|
| Light | 灯光设备 | 智能灯泡、灯带 |
| Switch | 开关设备 | 墙壁开关、插座 |
| Sensor | 传感器 | 温湿度、光照 |
| Binary Sensor | 二元传感器 | 门窗、人体检测 |
| Climate | 空调/温控 | 空调伴侣、温控器 |
| Cover | 窗帘 | 智能窗帘电机 |
| Remote | 遥控器 | 万能遥控器 |
| Event | 事件 | 按钮点击、手势 |
| Air Quality | 空气质量 | 空气检测仪 |
| Button | 按钮 | 场景按钮 |
| Number | 数字输入 | 数值调节 |
| Select | 选择器 | 模式选择 |

## 自动化示例

### 示例1: 门窗传感器触发灯光

```yaml
automation:
  - alias: "门打开时开灯"
    trigger:
      - platform: state
        entity_id: binary_sensor.aqara_door_sensor
        to: "on"
    action:
      - service: light.turn_on
        target:
          entity_id: light.aqara_bedroom_light
```

### 示例2: 温度控制空调

```yaml
automation:
  - alias: "温度过高开空调"
    trigger:
      - platform: numeric_state
        entity_id: sensor.aqara_temperature
        above: 26
    action:
      - service: climate.set_temperature
        target:
          entity_id: climate.aqara_ac
        data:
          temperature: 24
          hvac_mode: cool
```

### 示例3: 无线开关控制场景

```yaml
automation:
  - alias: "开关单击切换灯光"
    trigger:
      - platform: event
        event_type: aqara_bridge_event
        event_data:
          entity_id: event.aqara_wireless_switch
          event: single
    action:
      - service: light.toggle
        target:
          entity_id: light.living_room
```

## 调试技巧

### 启用详细日志

在 `configuration.yaml` 中添加：

```yaml
logger:
  default: warning
  logs:
    custom_components.aqara_bridge: debug
    custom_components.aqara_bridge.core.aiot_cloud: debug
    custom_components.aqara_bridge.core.aiot_manager: debug
```

### 查看日志

1. 设置 → 系统 → 日志
2. 搜索 "aqara_bridge"
3. 查看错误信息和消息推送情况

### 常见日志信息

- `Received message`: 收到设备消息推送
- `Device state updated`: 设备状态已更新
- `Token expired`: Token过期，需要重新授权
- `API call failed`: API调用失败，检查网络和凭证

## 性能优化

### 减少API调用

Aqara云端API有调用频率限制，建议：

- ❌ 不要设置过于频繁的状态轮询
- ✅ 依赖消息推送获取状态更新
- ✅ 合理设置自动化触发条件

### 网络优化

- 确保Home Assistant能访问Aqara云端服务器
- 如使用中国服务器，确保网络稳定
- 考虑使用有线网络而非WiFi

## 故障排除

### 问题: 设备不显示

**解决方案**:
1. 确认设备已绑定到Aqara账号
2. 检查设备是否在线
3. 重新加载集成
4. 查看日志是否有错误

### 问题: 无法控制设备

**解决方案**:
1. 检查token是否过期（重新授权）
2. 确认消息推送配置正确
3. 检查设备是否支持云端控制
4. 查看日志中的API调用结果

### 问题: 状态不更新

**解决方案**:
1. 确认消息推送已启用"全订阅"
2. 检查网络连接
3. 重启Home Assistant
4. 查看日志中的消息接收情况

## 安全建议

⚠️ **保护你的凭证**:
- 不要在公开场合分享App ID、App Key、Key ID
- 不要将包含凭证的配置文件上传到公开仓库
- 定期更换密钥（在开发者平台操作）

⚠️ **网络安全**:
- 使用HTTPS访问Home Assistant
- 启用防火墙保护
- 定期更新Home Assistant版本

## 获取帮助

如遇到问题：

1. 查看 [README.md](README.md) 了解基本信息
2. 查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新
3. 检查日志获取错误信息
4. 提交Issue并附上日志信息
