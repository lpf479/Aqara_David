# GitHub仓库设置指南

## 发布前必须修改的文件

在将项目推送到GitHub之前，需要将以下文件中的占位符替换为实际的仓库信息。

### 1. manifest.json

**文件路径**: `custom_components/aqara_bridge/manifest.json`

**需要替换**:
```json
"documentation": "https://github.com/YOUR_USERNAME/YOUR_REPO",
"issue_tracker": "https://github.com/YOUR_USERNAME/YOUR_REPO/issues",
```

**替换为**（示例）:
```json
"documentation": "https://github.com/david/aqara-bridge-enhanced",
"issue_tracker": "https://github.com/david/aqara-bridge-enhanced/issues",
```

### 2. README.md

**文件路径**: `README.md`

**需要替换**（第3行）:
```markdown
[![version](https://img.shields.io/badge/version-26.2.24.2-blue.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/releases)
```

**替换为**（示例）:
```markdown
[![version](https://img.shields.io/badge/version-26.2.24.2-blue.svg)](https://github.com/david/aqara-bridge-enhanced/releases)
```

### 3. INSTALL.md

**文件路径**: `INSTALL.md`

**需要替换**（第5行）:
```bash
git clone <your-repo-url>
```

**替换为**（示例）:
```bash
git clone https://github.com/david/aqara-bridge-enhanced.git
```

## 快速替换命令

创建GitHub仓库后，使用以下命令批量替换：

```bash
# 进入项目目录
cd /Users/david/Desktop/Homeassistant/Aqara_David

# 设置你的GitHub用户名和仓库名
GITHUB_USER="your_username"
REPO_NAME="your_repo_name"

# 批量替换（macOS）
find . -type f \( -name "*.md" -o -name "*.json" \) -exec sed -i '' "s|YOUR_USERNAME/YOUR_REPO|${GITHUB_USER}/${REPO_NAME}|g" {} +
find . -type f -name "*.md" -exec sed -i '' "s|<your-repo-url>|https://github.com/${GITHUB_USER}/${REPO_NAME}.git|g" {} +

# 验证替换结果
grep -r "YOUR_USERNAME" .
grep -r "your-repo-url" .
```

如果上述命令没有输出，说明替换成功。

## 检查清单

发布前请确认：

- [ ] manifest.json中的documentation和issue_tracker已更新
- [ ] README.md中的徽章链接已更新
- [ ] INSTALL.md中的git clone命令已更新
- [ ] 所有"YOUR_USERNAME/YOUR_REPO"已替换
- [ ] 所有"<your-repo-url>"已替换

## 当前配置

**集成名称**: Aqara Bridge Enhanced
**版本**: 26.2.24.2
**Domain**: aqara_bridge

在Home Assistant中显示为: **Aqara Bridge Enhanced**

## 注意事项

1. **不要修改domain**: `aqara_bridge`必须保持不变，否则会导致兼容性问题
2. **版本号格式**: 保持`26.2.24.2`格式，后续更新时递增
3. **文档链接**: 确保链接指向你的实际仓库，否则用户无法获取帮助

## 发布后验证

1. 在HACS中添加自定义仓库
2. 检查集成名称是否显示为"Aqara Bridge Enhanced"
3. 点击文档链接，确认能正确跳转
4. 提交Issue测试，确认issue_tracker链接正确
