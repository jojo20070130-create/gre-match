# GRE 等价词速配

这是一个单文件的 GRE 等价词配对小游戏，当前在 GitHub Pages 上托管。

## 本地打开

1. 在仓库根目录双击打开 `index.html`，浏览器会直接读取本地页面。
2. 如果你想在本地用 HTTP 方式打开，也可以运行：

   ```bash
   cd /Users/jojoz/Desktop/gre-match
   python3 -m http.server 8000
   ```

   然后访问 `http://localhost:8000/`。

## 词库结构

- `data/words.js`：单词词条，键是单词，值是 `{ def, zh }`。
- `data/synonyms.js`：等价词配对，保持与原来 `groups` 顺序一致。

## 加一对新等价词

1. 在 `data/synonyms.js` 里新增一条：

   ```js
   { "group": 11, "a": "new_word", "b": "synonym", "zh": "中文" }
   ```

2. 在 `data/words.js` 里补上这两个词的词条：

   ```js
   "new_word": { "def": "英文释义", "zh": "" },
   "synonym": { "def": "英文释义", "zh": "" }
   ```

3. 只改数据，不改游戏逻辑和外观即可。

## 提交前注意

- 先确保本地打开页面正常。
- 先确认右键释义和背单词列表仍然能用。
- 提交前不要改动 `localStorage` 的 key。
- 只在你确认数据顺序与原来一致时再提交。
