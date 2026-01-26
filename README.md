# LangChain 学习项目

## 项目概述

本项目是一个 LangChain 学习实践项目，涵盖了文档加载、文本分割、向量存储、对话记忆等核心功能的实现和调试过程。

## 项目结构

```
f:\ragtest/
├── 1.py                          # 基础文档加载和文本分割
├── 2.py                          # 对话记忆系统（pickle序列化）
├── 3.py                          # 纯文本存储的对话记忆
├── 3.纯文本长期回话记忆chat_history1.py  # 纯文本存储的完整实现
├── JsonOutputPraser.py           # JSON输出解析器
├── langchain调用ollama的chatmodels.py  # Ollama集成
├── preprocess_csv.py             # CSV预处理工具
├── test.csv                      # 测试数据
├── test.txt                      # 测试文本
├── stus.json                     # 学生数据
├── README.md                     # 项目说明
└── chat_history/                 # 对话历史存储目录
```

## 核心功能

### 1. 文档加载与处理
- **TextLoader**: 加载纯文本文件
- **CSVLoader**: 加载CSV文件（支持自定义分隔符）
- **PyPDFLoader**: 加载PDF文件（推荐，稳定性好）
- **UnstructuredPDFLoader**: 高级PDF加载（依赖复杂，易出错）

### 2. 文本分割
- **RecursiveCharacterTextSplitter**: 智能文本分割
- 支持中文标点符号分割
- 可配置chunk_size和chunk_overlap

### 3. 向量存储与检索
- **InMemoryVectorStore**: 内存向量存储
- **Chroma**: 向量数据库（依赖复杂，版本兼容性差）
- 支持相似性搜索和文档检索

### 4. 对话记忆系统
- **短期记忆**: 基于会话的上下文记忆
- **长期记忆**: 文件持久化存储
- **多种存储格式**:
  - Pickle序列化（二进制，高效）
  - 纯文本存储（人类可读，易调试）
  - JSON格式（结构化，但复杂）

### 5. 模型集成
- **通义千问**: DashScope/阿里云百炼API
- **Ollama**: 本地模型部署
- **OpenAI兼容API**: 支持多种模型

## 重难点总结

### 1. JSONLoader的使用
```python
# JSONPath表达式
"."  # 根节点
".name"  # 所有name字段
".[0].name"  # 第一个对象的name字段
".[1:3]"  # 索引1-2的对象
```

### 2. 依赖管理问题
- **NumPy版本冲突**: 二进制扩展模块损坏
- **ChromaDB兼容性**: 需要Python 3.9+
- **Unstructured库**: 依赖链复杂，易DLL失败
- **解决方案**: 使用PyPDFLoader替代，降级版本

### 3. 编码问题
- 中文注释需要UTF-8编码声明
- CSV文件编码处理（GBK vs UTF-8）
- 文件路径中的中文处理

### 4. 消息格式处理
- **变量名匹配**: ChatPromptTemplate的变量必须一致
- **消息类型**: human/ai/system消息的正确处理
- **文本格式解析**: 纯文本存储的格式验证

### 5. 会话管理
- **session_id作用**: 隔离不同对话会话
- **历史记录格式**: 消息对象的序列化与反序列化
- **存储格式选择**: 性能vs可读性的权衡

## 常见错误及解决方案

### 1. 模块导入错误
```
ModuleNotFoundError: No module named 'xxx'
```
**解决**: 使用清华源安装缺失依赖
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
```

### 2. 版本兼容性问题
```
TypeError: 'type' object is not subscriptable
```
**解决**: 升级Python到3.9+或降级相关库

### 3. 编码错误
```
SyntaxError: Non-UTF-8 code starting with '\xb1'
```
**解决**: 添加编码声明或删除中文注释

### 4. 变量不匹配
```
KeyError: "Input to ChatPromptTemplate is missing variables {'content'}"
```
**解决**: 确保模板变量与实际传入变量一致

### 5. 文件格式错误
```
ValueError: not enough values to unpack (expected 2, got 1)
```
**解决**: 添加格式验证和异常处理

## 最佳实践建议

1. **依赖管理**: 优先使用PyPDFLoader，避免Unstructured复杂依赖
2. **错误处理**: 添加充分的异常处理和格式验证
3. **编码统一**: 统一使用UTF-8编码，避免中文注释问题
4. **版本控制**: 固定关键依赖版本，避免兼容性问题
5. **存储选择**: 根据需求选择存储格式（pickle/文本/JSON）
6. **调试技巧**: 使用print_prompt函数查看实际提示内容

## 运行环境要求

- Python 3.8+ (推荐3.9+)
- 主要依赖:
  - langchain
  - langchain-community
  - numpy
  - pandas
  - pydantic

## 联系方式

如有问题或建议，欢迎提出Issue或Pull Request。