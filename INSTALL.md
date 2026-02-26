# 快速安装指南

## 手动安装步骤

1. **下载此仓库**
   ```bash
   git clone https://github.com/lpf479/Aqara_David.git
   ```

2. **复制到Home Assistant配置目录**
   ```bash
   cp -r Aqara_David/custom_components/aqara_bridge /path/to/homeassistant/config/custom_components/
   ```

3. **重启Home Assistant**

4. **添加集成**
   - 进入 设置 → 设备与服务 → 添加集成
   - 搜索 "Aqara Bridge"
   - 按照提示输入开发者账号信息

## HACS安装步骤

1. **添加自定义存储库**
   - HACS → Integrations → 右上角菜单 → Custom repositories
   - 添加仓库URL
   - 类别: Integration

2. **安装集成**
   - 搜索 "Aqara Bridge"
   - 点击安装

3. **重启并配置**
   - 重启Home Assistant
   - 按照上述步骤4添加集成

## 所需信息

在配置前，请准备好以下信息：

- ✅ Aqara账号（手机号或邮箱）
- ✅ 国家代码（CN/USA/KR/RU/GER）
- ✅ App ID（从开发者平台获取）
- ✅ App Key（从开发者平台获取）
- ✅ Key ID（从开发者平台获取）

详细的开发者账号申请流程请参考 [README.md](README.md)
