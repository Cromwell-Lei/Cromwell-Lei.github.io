# Chenjun Lei — Personal Archive

一个纯静态个人主页，展示研究、项目、职业经历、摄影及个人兴趣。视觉方向为 The Considered Archive：冷白底、石墨文字、编辑式排版和原创 CSS 几何图形。

- 网站：https://cromwell-lei.github.io/
- 仓库：https://github.com/Cromwell-Lei/Cromwell-Lei.github.io
- 部署：GitHub Pages，`main` 分支根目录。
- 技术：HTML、CSS、Vanilla JavaScript；没有 npm、构建工具、数据库、第三方字体、API 或 secret。

## 内容状态

目前是可使用的完整网站框架。职业头衔采用已确认的 **Data Engineer at Chuchiang Data**。论文、项目详情、任职日期、教育经历、真实摄影作品、CV、邮箱和 LinkedIn 地址尚未补充，页面明确标注 forthcoming / to be added。不要把占位文字当作已发表论文或已完成项目。

所有装饰图形由 CSS 绘制，不是真实摄影或研究数据。无效的联系方式和 CV 不设置假链接。

## 文件结构

- `index.html`：首页精选、About、职业经历、兴趣、联系方式。
- `research.html`：研究档案；以后添加论文、摘要、状态、Paper / Code / Data。
- `projects.html`：数据工程与数字产品案例结构。
- `photography.html`：六个摄影占位，未来完整摄影画廊。
- `css/style.css`：全站颜色、字体、响应式、打印样式、reduced motion。
- `js/main.js`：自动年份、当前章节提示、旧锚点兼容、真实照片放大查看。
- `assets/images/`：未来真实照片。
- `assets/icons/favicon.svg`：浏览器图标。
- `404.html`：自定义错误页（资源使用根路径，支持任意深度的错误 URL）。
- `robots.txt`、`sitemap.xml`：搜索引擎入口。
- `.nojekyll`：直接发布静态文件，不要求 Jekyll 处理。

## 本地预览

在仓库根目录运行（需安装 Python 3，无需安装第三方包）：

```sh
python3 -m http.server 8000
```

然后访问 http://localhost:8000 。普通页面也可以直接打开 HTML，但请用本地服务器检查 404 页的根路径资源。Python 的简单服务器不会自动把不存在路径交给自定义 404；可直接预览 /404.html，最终 HTTP 404 行为由 GitHub Pages 验证。

## 修改个人介绍和职业经历

编辑 `index.html` 的 `id="lei-experience"` 部分：

- `.about-copy` 是个人介绍。
- `.job` 是一条经历，可以复制增加；按时间倒序排列。
- 用真实起止年月替换 DATES TO ADD。
- 职位更改时，同时修改首页 Hero 的 `.role` 及 meta description。
- 添加教育经历时单独标为 Education，避免与工作混在一起。

## 修改研究成果

编辑 `research.html`。每条成果建议包含：题目、作者、年份、期刊/会议、准确状态、短摘要和可访问的材料链接。

```html
<article class="record">
  <div class="meta"><span>YEAR / VENUE</span><span>VERIFIED STATUS</span></div>
  <h3>Actual paper title</h3>
  <p>Author list and one-sentence contribution.</p>
  <details>
    <summary>Abstract</summary>
    <p>The real abstract.</p>
  </details>
  <!-- Add Paper / Code / Data links only when the destination exists. -->
</article>
```

已发表、已接收、预印本和在研必须分别标注，不把投稿中写成已发表。补完以后移除本页对应的占位提示，并在 `index.html#lei-research` 更新精选摘要。

## 修改项目

编辑 `projects.html` 中的 `#data-engineering` 和 `#digital-products`；首页精选入口位于 `index.html#lei-projects`。

按“问题 → 我的贡献 → 方法与决策 → 结果与限制”组织案例。只使用核实后的量化结果，不公布客户机密。如果项目很多，可以增加 `projects/project-name.html`，同时调整资源相对路径、导航、canonical 和 sitemap。

## 添加摄影作品

1. 将照片放进 `assets/images/`，文件名小写，不含空格；建议 WebP/JPEG，长边 1600–2400px。
2. 发表前确认版权并移除照片中的 GPS 等不必要的个人元数据。
3. 在 `photography.html` 中把一张 `.photo-frame` 占位替换为下面的链接和图片。保留外面的 figure，并写真实图注。

```html
<figure>
  <a class="photo-link" data-lightbox href="assets/images/canberra-evening.webp">
    <img src="assets/images/canberra-evening.webp"
         alt="Describe the actual scene, not just the filename"
         width="1600" height="2000" loading="lazy" decoding="async">
  </a>
  <figcaption><span>Real title</span><span>Place / Year</span></figcaption>
</figure>
```

`width` 和 `height` 应写原图真实尺寸。缩略图默认 object-fit: cover；放大后 object-fit: contain，不裁切原图。需要不同缩略图比例时给图片增加对应 CSS class。

带 `data-lightbox` 的真实照片会启用原生 dialog 查看器：Esc 关闭、左右键切换、关闭后焦点返回原链接。不支持 dialog 或关闭 JavaScript 时仍可通过普通链接打开图片。占位框不冒充可点击作品。

首页 `#lei-outside` 可放三张精选，完整画廊仍保留全部作品。每次上传后删除已被替换的占位文字；没有照片的剩余位置可以继续保留或删减。

## 修改兴趣与联系方式

- 兴趣：`index.html#lei-outside` 的 `.interests`，及 `photography.html` 底部。
- 联系方式：`index.html#lei-contact` 的 `.contact-list`。
- 邮箱确认后使用 `<a href="mailto:真实邮箱">真实邮箱</a>`。
- LinkedIn 使用你自己的完整个人主页 URL，不用平台首页。
- 外链新窗口需 `target="_blank" rel="noopener noreferrer"`，并在可访问名称中说明新窗口。
- CV：先上传真实 PDF 到 `assets/documents/cv.pdf`，再将 CV forthcoming 替换为有效链接；不要先放一个不存在的下载地址。

## 调整视觉和交互

`css/style.css` 开头的变量控制背景、文字、分隔线和强调色。字体为系统字体，不会向第三方发送字体请求。

- 断点覆盖桌面、平板和手机，摄影网格会重排而不是隐藏作品。
- 动画约 200–240ms；尊重 `prefers-reduced-motion`。
- 正文不会依赖入场动画才能出现。
- 保留清楚的键盘焦点、跳过导航链接和语义标题。
- JS 不请求外部服务，不保存访问者信息，无分析追踪。

## 部署和回滚

```sh
git add index.html research.html projects.html photography.html css js assets README.md sitemap.xml
git commit -m "content: update personal archive"
git push origin main
```

GitHub Settings → Pages：Source 为 Deploy from a branch，branch 为 main，目录为 / (root)。Push 后 GitHub 自动运行内置 Pages 发布流程；本项目不需要自建 Actions workflow 或任何 secret。

等待仓库 Actions 中的 `pages build and deployment` 成功，再打开网站验证。改 CSS/JS 后更新各 HTML 的 `?v=3` 版本号可避免旧浏览器缓存。不要以一次 push 成功代替部署检查。

需要回滚时使用 `git revert <commit-sha>` 创建反向提交再 push，不使用 force push。部署会重新发布回滚后的版本。

## 每次更新检查

- 检查 1440、1024、768、390、320px 宽度，确保没有横向溢出。
- 键盘 Tab 可到所有链接；焦点可见；研究摘要能展开/收起。
- 照片查看器支持 Esc、左右键和焦点恢复。
- 关闭 JavaScript 时正文、导航和真实图片链接仍能用。
- 首页、三张档案页、CSS、JS、favicon 都返回 200。
- 访问一个不存在的深层路径，应该返回 HTTP 404 并显示自定义错误页。
- 新增页面同步 title、description、canonical、Open Graph 和 sitemap。
- 不提交 token、密码、用户数据、私人材料或开发验收文件。
