"""Generate the bilingual static archive. Run: python3 scripts/build.py"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://cromwell-lei.github.io/'
def pair(en, zh): return {'en': en, 'zh': zh}

papers = [
 dict(id='synstress', year='2026', title='Stress-conditioned synthetic data for robust credit-risk model validation under rare economic scenarios', authors='Chenjun Lei, Chengxiao Dai', venue='Scientific Data', status=pair('Submitted', '投稿中'), summary=pair('Synthetic credit data conditioned on rare economic scenarios, designed to test how default-risk models behave under stress.', '面向罕见经济情景生成信用合成数据，检验违约风险模型在压力条件下的表现。'), detail=pair('Combines borrower and loan histories with macroeconomic indicators. Validation compares discrimination, calibration and stress sensitivity across baseline and adverse scenarios. This manuscript is submitted to Scientific Data; a public manuscript link is not yet available.', '结合借款人、贷款历史与宏观经济指标，比较模型在基准与压力情景下的区分度、校准度和压力敏感性。稿件已投至 Scientific Data，目前暂无可核实的公开原文链接。')),
 dict(id='safe-remediation', year='2026', title='Safe Remediation as Risk-Constrained Intervention Decision in Microservice Systems', authors='Chengxiao Dai, Zhaokun Yan, Chenjun Lei, Qiao Li, Luyan Zhang', venue='IEEE SMC 2026', status=pair('Accepted · preprint available', '已接收 · 预印本可读'), arxiv='2607.20005', summary=pair('Deciding when an automated repair is safe enough to execute, when to gather evidence, and when to involve a human.', '让自动修复系统判断何时可以执行、何时需要更多证据，以及何时应交由人工处理。'), detail=pair('Models intervention as a constrained decision process, with risk assessed through blast radius, reversibility and uncertainty. On the Train Ticket benchmark, the paper reports a 39% reduction in false remediation and a 2.5-point improvement in repair success over a strong runbook baseline; escalation load falls 17% against a fixed-threshold variant.', '将修复干预建模为受约束的决策过程，从影响范围、可逆性和不确定性评估风险。在 Train Ticket 基准上，论文报告相较强运行手册基线，错误修复率降低 39%，修复成功率提高 2.5 个百分点；相较固定阈值方案，人工升级处理负荷降低 17%。')),
 dict(id='coordinating-memory', year='2026', title='Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing', authors='Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang', venue='IEEE SMC 2026', status=pair('Accepted · preprint available', '已接收 · 预印本可读'), arxiv='2607.19985', summary=pair('Reusing the structure of past coordination experience to help manufacturing agents adapt to new disruptions.', '复用历史协作经验中的关系结构，帮助制造系统中的多个智能体适应新的扰动。'), detail=pair('Stores past coordination episodes as relational graphs and retrieves structurally similar experience for policy adaptation. On dynamic flexible job-shop benchmarks, the paper reports 4.1–10.0% shorter makespan and 33–38% faster adaptation than the strongest memory-augmented baseline, across three disturbance types.', '将历史协作过程存为关系图，检索结构相似的经验以支持策略适应。在动态柔性作业车间基准的三类扰动下，论文报告相较最强的记忆增强基线，最大完工时间缩短 4.1–10.0%，适应时间缩短 33–38%。')),
 dict(id='labour-report',year='2025',title=pair('Migrant Labour Employment Frictions and Economic Efficiency','外籍员工雇佣摩擦与经济效率研究'),authors=pair('Chenjun Lei · Project member','雷晨俊 · 项目成员'),venue=pair('Macao Foundation · Research report','澳门基金会 · 研究报告'),status=pair('Research report','研究报告'),summary=pair('Research on migrant labour, employment frictions and economic efficiency in Macao.', '围绕澳门外籍劳工、雇佣摩擦与经济效率开展研究。'),detail=pair('Contributed as a project member to research and report preparation. The associated research-assistant work covered survey design, data cleaning, regression analysis and policy recommendations.', '作为项目成员参与研究与报告撰写；相关研究助理工作涵盖问卷设计、数据清洗、回归分析与政策建议。'))
]

projects = [
 dict(id='synthetic-platform',date='07/2026',title=pair('Financial synthetic data & anonymisation platform','金融合成数据与数据脱敏集成平台'),tag=pair('Data products / Financial infrastructure','数据产品 / 金融基础设施'),metric=pair('11 modules','11 个模块'),intro=pair('An industry-configurable workflow for anonymisation, privacy protection and expansion of small financial datasets.','面向金融场景，将脱敏、隐私保护与小规模数据扩容整合为可按行业配置的工作流。'),parts=[
 pair('Designed an 11-module architecture covering data import, processing, validation and export, with configurable industry workflows.','设计包含 11 个模块的平台架构与模块化工作流，覆盖数据导入、处理、验证与导出，支持按行业场景配置。'),
 pair('Translated financial-data anonymisation techniques and client model-development requirements into product specifications; worked with technical teams on de-identification, synthetic augmentation and financial-data applications.','将金融数据安全脱敏技术与客户模型开发需求转化为产品方案，配合技术团队设计脱敏、合成扩容及金融数据应用场景。'),
 pair('Designed modular interfaces, configuration logic and validation rules for financial institutions and system integrators, supporting integration with downstream risk-control models and data-security systems.','根据金融机构及系统集成商需求设计模块接口、配置逻辑与验证规则，推动与下游风控模型和数据安全系统集成。')]),
 dict(id='annotation-platform',date='07/2026',title=pair('Commercial data annotation & work platform','商用数据标注交易与作业平台'),tag=pair('Product design / Expert workflows','产品设计 / 专家作业'),metric=pair('End-to-end workflow','全流程设计'),intro=pair('Product and commercial design connecting client requests, expert work, quality review and delivery.','连接客户需求、专家作业、质量审核与成果交付的产品及商业模式设计。'),parts=[
 pair('Researched domestic and international approaches; designed the workflow from requirement submission and task decomposition to assignment, quality checks and delivery.','调查国内外成熟方案，设计从客户需求发布、任务拆解、接单作业到质检返工及成果交付的完整业务流程。'),
 pair('Localised task classification, review, expert annotation operations and payment mechanisms for different requirements.','按不同需求类型建立任务池分类、质量审核、本地标注作业系统与支付机制。'),
 pair('Developed pricing and settlement rules around client charges, task settlement and platform services; used market and competitor analysis to inform differentiation and feature priorities.','围绕客户收费、任务结算及平台服务模式制定定价与结算规则；分析主流平台的功能、流程及商业模式，支持差异化定位与功能优先级决策。')]),
 dict(id='credit-risk',date='08/2026',title=pair('Stress-conditioned credit-risk model validation','极端经济情景下的信用风险模型验证'),tag=pair('Research / Synthetic data','研究 / 合成数据'),metric=pair('Rare economic scenarios','罕见经济情景'),intro=pair('A synthetic-data framework for evaluating credit-risk models when historical data contain too few extreme conditions.','针对历史样本中极端金融情景不足的问题，构建压力条件合成数据框架以检验模型稳健性。'),parts=[
 pair('Collected and cleaned borrower- and loan-level credit histories together with gross domestic product, unemployment, interest rates, inflation and housing-price indicators.','收集并清洗借款人及贷款层面的历史信用数据，以及国内生产总值（GDP）、失业率、利率、通胀和房价等宏观经济指标。'),
 pair('Generated rare or unobserved stress scenarios and compared probability of default (PD) models under baseline and adverse conditions to identify degradation, calibration drift and instability.','生成历史中稀缺或未出现的极端情景，对违约概率（Probability of Default，PD）模型在基准与压力条件下进行比较，识别性能衰减、校准漂移及稳定性差异。'),
 pair('Built an evaluation framework spanning discrimination, calibration and stress sensitivity, and proposed reusable synthetic-data methods for assessing performance in extreme conditions.','建立覆盖区分度、校准度及压力敏感性的模型验证指标体系，比较不同模型的失效模式并提出可复用的合成数据方法。')]),
 dict(id='domain-datasets',date='05/2026',title=pair('Domain datasets for Alibaba Cloud language-model fine-tuning','阿里云大语言模型学科微调数据集'),tag=pair('Training data / Quality assurance','训练数据 / 质量管理'),metric=pair('900 accepted questions','900 条合格题目'),intro=pair('Specialist fine-tuning material in finance, astronomy and physics, built with expert review and consistent quality standards.','面向金融、天文与物理领域，组织学科专家构建专业微调数据，并以统一标准检验质量。'),parts=[
 pair('Coordinated external experts to create difficult subject-specific questions and validated standard answers; delivered 900 accepted questions across the three disciplines.','组织外部专家设计高难度学科问题及经验证的标准答案，三学科合格交付题目达到 900 条。'),
 pair('Designed a production workflow covering source collection, task standards, expert review and consistency checks to improve training and evaluation data reliability.','设计覆盖数据源收集、任务标准、专家复核与一致性检查的端到端数据生产流程，提升训练及评测数据可靠性。'),
 pair('Defined quality criteria and sampling checks for difficulty, answer correctness, formatting consistency and domain validity.','制定题目难度、答案正确性、格式一致性及领域有效性的质量标准与抽检机制，支持专业语料的规模化交付。')])
]

jobs = [
 dict(date='12/2025 — 08/2026',org=pair('Chuchiang Data','珠江数据'),role=pair('FinTech Product Manager','金融科技产品经理'),place=pair('Shanghai, China','中国 · 上海'),points=[
 pair('Participated end to end in 2 products and contributed to 5 further FinTech and data-software products, covering market research, competitor analysis, architecture, module design, team coordination and launch planning.','全程参与 2 个、部分参与 5 个金融科技与数据软件产品开发，工作涵盖市场调研、竞品分析、产品架构、模块设计、团队协作、上线规划与市场进入执行。'),
 pair('Led agile delivery for 2 products, coordinating R&D, data, sales and delivery teams; iterated weekly using client feedback and back-office usage data.','主导 2 款产品的敏捷开发，协调研发、数据、销售及交付团队，以周为周期开展需求评审，并结合客户反馈与后台使用数据持续调整服务。'),
 pair('Translated system-integrator requirements in information disclosure and payment security into deployable products; supported commercial contracts and deployment in 7 data-security-centre systems.','将系统集成商在信息披露及支付安全场景中的需求转化为可部署产品，推动商业签约并完成在 7 个数据安全中心系统中的落地。'),
 pair('Designed commercial and risk-control plans for 2 FinTech products, including subscription and buyout options for smaller businesses and cloud providers, deployment, cost and security-compliance requirements.','对 2 款产品进行商业化及风控设计，为中小企业与云服务商分别制定订阅及买断方案，并结合客户规模、部署方式、交付成本及数据安全合规要求参与定价与交付方案设计。')]),
 dict(date='07/2024 — 09/2024',org=pair('ShineWing','信永中和'),role=pair('Financial Audit','金融审计'),place=pair('Beijing, China','中国 · 北京'),points=[
 pair('Contributed to external audits for 3 multi-industry listed companies and central state-owned enterprises; used reconciliation, sampling, interviews and variance analysis to identify unusual movements, inconsistent data, compliance issues and potential financial risks.','参与 3 家行业龙头上市公司和央企的外部审计，收集并分析财务数据及重点科目，通过对账、抽样、访谈与差异分析识别异常波动、数据不一致、违规操作及潜在财务风险。'),
 pair('Tested internal controls across revenue, procurement, receivables, payables and cash flows, tracing source documents to accounting records to assess completeness and control effectiveness.','对收入、采购、应收应付及现金流等核心财务流程开展内部控制测试，从原始凭证追溯至会计记录，评估数据完整性及控制有效性。'),
 pair('Cross-checked ledgers, bank statements, invoices, contracts and business records; worked with client finance teams to resolve gaps and supported 5 audit reports delivered on schedule.','交叉核对总账、银行流水、发票、合同及业务资料，与客户财务团队解决数据缺口，协助撰写 5 份审计报告，支持审计结论按期形成并交付。')]),
 dict(date='05/2023 — 07/2025',org=pair('Finance Laboratory, City University of Macau','澳门城市大学金融实验室'),role=pair('Research Assistant','研究助理'),place=pair('Macao, China','中国 · 澳门'),points=[
 pair('Contributed to 4 projects on construction, migration and migrant labour. Surveyed or interviewed 100+ construction firms, industry unions and government bodies; analysed 160,000+ migrant-labour records and maintained survey response rates at 30% across projects.','参与 4 个研究项目，围绕建筑业、移民及外籍劳工等社会问题开展统计分析；调研或访谈 100+ 家建筑企业、行业工会及政府机构，分析 16 万+ 外籍劳工记录，实现各项目统计问卷回收率稳定在 30%。'),
 pair('Worked across survey distribution and collection, data cleaning, regression, statistical analysis and visualisation to produce more than 20 portraits, reports and charts using Excel, Stata, R, Python, SPSS and Power BI.','负责研究全周期，通过问卷发放与回收、数据清洗、回归与统计分析及可视化，形成 20 份以上研究对象画像、报告及图表；使用 Excel、Stata、R、Python、SPSS 与 Power BI 完成建模和分析。'),
 pair('Helped write research reports and policy recommendations; represented the university as an industry–academia participant alongside the Macao Foundation in regulatory-revision participation and a Macao Legislative Assembly inquiry.','利用研究结果协助撰写报告及政策建议；代表学校以业界学者身份，配合澳门基金会参与相关法规修改建议及澳门特别行政区立法会质询。')]),
 dict(date='07/2023 — 09/2023',org=pair('Guoyuan Securities','国元证券'),role=pair('Debt Underwriting Intern','债券承销实习生'),place=pair('Fujian, China','中国 · 福建'),points=[
 pair('Supported a RMB 150 million bond issuance for a state-owned steel enterprise, preparing due-diligence materials, reviewing collateral and collecting source documents.','参与某国有钢铁企业 1.5 亿元人民币债券发行项目，协助整理尽调材料、核查抵押物、收集原始资料并准备发行文件。'),
 pair('Coordinated information among internal teams, issuers, auditors, legal advisers and credit-rating agencies, supporting audit reports, legal opinions and rating reports.','协调团队成员、发行人、审计机构、法律顾问及信用评级机构的信息流转，汇总资料并支持审计报告、法律意见书及评级报告的形成。'),
 pair('Prepared debt-structure statistics and issuance-discussion materials; supported information exchange on issue size, coupon rates, issuance strategy and regulatory communication.','整理统计数据并准备债务结构及发行讨论材料，参与发行规模、票面利率、发行策略及监管沟通相关的信息交换与支持。')])
]

def text(value, lang): return value[lang] if isinstance(value, dict) else value
def e(value, lang): return escape(text(value,lang))
def ul(values,lang): return '<ul class="detail-list">'+''.join('<li>'+e(v,lang)+'</li>' for v in values)+'</ul>'
def link(href,label): return f'<a class="text-link" href="{href}">{label} ↗</a>'
def paper(p,lang,full=False):
    tr=lambda a,b: a if lang=='en' else b
    title=e(p['title'],lang); authors=e(p['authors'],lang).replace('Chenjun Lei','<strong>Chenjun Lei</strong>').replace('雷晨俊','<strong>雷晨俊</strong>')
    if 'arxiv' in p: title=f'<a href="https://arxiv.org/abs/{p["arxiv"]}">{title}</a>'
    s=f'<article class="record publication" id="{p["id"]}"><div class="meta"><span>{p["year"]} / {e(p["venue"],lang)}</span><span class="status">{e(p["status"],lang)}</span></div><h3 lang="{"zh-CN" if lang=="zh" and isinstance(p["title"],dict) else "en"}">{title}</h3><p class="authors">{authors}</p><p>{e(p["summary"],lang)}</p>'
    if full:
        if 'arxiv' in p: s+=f'<p class="venue-name">2026 IEEE International Conference on Systems, Man, and Cybernetics</p>'
        s+=f'<details><summary>{tr("Research summary & findings","研究简介与结果")}</summary><p>{e(p["detail"],lang)}</p></details>'
    if 'arxiv' in p:
        s+='<div class="paper-links">'+link('https://arxiv.org/abs/'+p['arxiv'],tr('Paper · arXiv','论文 · arXiv'))+link('https://arxiv.org/pdf/'+p['arxiv'],'PDF')
        if full: s+=link(('../' if lang=='zh' else '')+'assets/citations/'+p['id']+'.bib','BibTeX')
        s+='</div>'
    elif full and p['id']=='synstress': s+=f'<p class="availability">{tr("Manuscript submitted; public paper and data links pending.","稿件投稿中，公开原文与数据链接待发布。")}</p>'
    return s+'</article>'

def chapter(id,num,label,title,body): return f'<section class="chapter" id="lei-{id}"><div class="chapter-label"><p class="kicker">{num} / {label}</p>{('<h2>'+title+'</h2>') if title else ''}</div><div>{body}</div></section>'
def education(lang):
    tr=lambda a,b:a if lang=='en' else b
    return f'''<div class="job"><span class="job-date">05/2026 — {tr('Present','至今')}</span><div><h3>{tr('Australian National University','澳大利亚国立大学')}</h3><p>{tr('Master of Economics','经济学硕士')}</p></div></div>
    <div class="job"><span class="job-date">09/2021 — 07/2025</span><div><h3>{tr('City University of Macau','澳门城市大学')}</h3><p>{tr('Bachelor of Applied Economics · Finance','应用经济学学士 · 金融方向')}</p><p class="job-note">{tr('Coursework: econometrics, economic and financial statistics, financial analysis, microeconomics, macroeconomics and financial derivatives.','主要课程：计量经济学、经济与金融统计、金融分析、微观与宏观经济学、金融衍生品。')}</p></div></div>'''
def skills(lang):
    tr=lambda a,b:a if lang=='en' else b
    groups=[(tr('Programming & data','编程与数据'),'Python · SQL · R · Stata · SPSS'),(tr('Analysis & visualisation','分析与可视化'),'Excel · Power BI · Tableau'),(tr('Product & delivery','产品与交付'),'Figma · Jira · Git · '+tr('Agile development · AI tools','敏捷开发 · AI 工具'))]
    return '<div class="skills-grid">'+''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a,b in groups)+'</div>'
def honors(lang):
    tr=lambda a,b:a if lang=='en' else b
    return ''.join(f'<div class="job"><span class="job-date">{y}</span><div><h3>{tr("Outstanding Research Team Scholarship","优秀科研团队奖学金")}</h3><p>{tr("City University of Macau · Awarded for outstanding research-team performance.","澳门城市大学 · 表彰优秀科研团队表现。")}</p></div></div>' for y in ('2025','2024'))
def job(j,lang,full=False):
    return f'<article class="job"><span class="job-date">{j["date"]}</span><div><h3>{e(j["org"],lang)}</h3><p>{e(j["role"],lang)} <span class="job-location">/ {e(j["place"],lang)}</span></p>{ul(j["points"],lang) if full else "<p class=\"job-note\">"+e(j["points"][0],lang)+"</p>"}</div></article>'
def interests(lang, include_photobook=False):
    tr=lambda a,b:a if lang=='en' else b
    cover=''
    if include_photobook:
        cover=f'<figure class="interest-feature"><img src="{"../" if lang=="zh" else ""}assets/images/world-stage-photobook.webp" alt="{tr("Cover of 世界皆舞台, a personal photobook.", "个人影集《世界皆舞台》封面。")}" width="1600" height="1200" loading="lazy"></figure>'
    entries=[
        (tr('Photography','摄影'),tr('Urban scenes, quiet light and everyday life. I am developing a personal photobook, 世界皆舞台 (All the World’s a Stage).','关注都市、光影与日常生活，正在筹备个人摄影作品集《世界皆舞台》。')),
        (tr('Music','音乐'),tr('Trumpet player in the Australian National University orchestra.','澳大利亚国立大学管弦乐团小号手。')),
        (tr('Motorsport & engineering','赛车与工程'),tr('Powertrain assembly engineer with the ANU Formula Sport team (ANUFS).','ANUFS 方程式赛车队内燃机动力总成工程师。'))
    ]
    return '<div class="interest-notes">'+''.join(f'<article><p class="kicker">{i:02}</p><h3>{a}</h3><p>{b}</p>{cover if i==1 else ""}</article>' for i,(a,b) in enumerate(entries,1))+'</div>'

def photo_carousel(lang, prefix=''):
    """A reusable carousel. Add future photographs to `slides` only."""
    tr=lambda a,b:a if lang=='en' else b
    slides=[
        ('fsae-australasia.webp', tr('FSAE Australasia competition', 'FSAE 澳大利亚赛事'), tr('ANU Formula Sport race car at FSAE Australasia competition.', 'FSAE 澳大利亚赛事上的 ANU Formula Sport 赛车。')),
        ('a-bad-days-happy.webp', tr("A bad day's happy", '坏日子里的快乐'), tr('A person resting on a swing under a bright blue sky.', '晴空下坐在秋千上的人。')),
        ('yamaha-ytr200dt.webp', 'YAMAHA YTR200DT', tr('A YAMAHA YTR200DT trumpet.', '一支 YAMAHA YTR200DT 小号。')),
        ('bicycle.webp', '', tr('A bicycle resting beneath yellow autumn trees.', '金色秋树下的一辆自行车。')),
        ('taipei-taiwan.webp', tr('Taipei, Taiwan', '台北，台湾'), tr('A Taiwan flag seen through an aeroplane window.', '透过飞机舷窗看到的台湾旗帜。')),
        ('sanming-china.webp', tr('Sanming, China', '中国三明'), tr('A night street scene in Sanming, China.', '中国三明的夜间街景。')),
        ('marina-bay-singapore.webp', tr('Marina Bay, Singapore', '新加坡滨海湾'), tr('Sunset over Marina Bay, Singapore.', '新加坡滨海湾的日落。')),
        ('fuji-japan.webp', tr('Fuji, Japan', '日本富士山'), tr('A summit marker on Mount Fuji, Japan.', '日本富士山顶的标志碑。')),
        ('canberra-australia.webp', tr('Canberra, Australia', '澳大利亚堪培拉'), tr('A bicycle beside Lake Burley Griffin in Canberra.', '堪培拉伯利·格里芬湖畔的一辆自行车。')),
        ('cityu-macau.webp', tr('Someday in CityU Macau', '澳门城市大学的某一天'), tr('Late sunlight through a City University of Macau stairwell.', '晚阳穿过澳门城市大学楼梯间。')),
    ]
    items=''.join(f'<figure class="carousel-slide" data-carousel-slide data-caption="{escape(s[1], quote=True)}"><img src="{prefix}assets/photos/{s[0]}" alt="{escape(s[2], quote=True)}" loading="lazy"></figure>' for s in slides)
    disabled=' disabled' if len(slides) < 2 else ''
    return f'<section class="photo-carousel" data-carousel aria-label="{tr("Photography carousel", "摄影作品轮播")}"><div class="carousel-viewport">{items}</div><div class="carousel-controls"><button type="button" data-carousel-prev aria-label="{tr("Previous photograph", "上一张照片")}"{disabled}>←</button><p class="carousel-count" data-carousel-count aria-live="polite">1 / {len(slides)}</p><button type="button" data-carousel-next aria-label="{tr("Next photograph", "下一张照片")}"{disabled}>→</button></div><p class="carousel-caption" data-carousel-caption>{slides[0][1]}</p></section>'

def render(lang,page,title,description,body):
    tr=lambda a,b:a if lang=='en' else b
    prefix='../' if lang=='zh' else ''
    path=('zh/' if lang=='zh' else '')+('' if page=='index' else page+'.html')
    enpath='' if page=='index' else page+'.html'
    other=('../'+enpath if lang=='zh' else 'zh/'+enpath)
    page_title=escape(title) if page=='index' else escape(title)+' — '+tr('Chenjun Lei','雷晨俊')
    og_title=escape(title) if page=='index' else escape(title)+' — Chenjun Lei'
    nav=''.join(f'<a href="{file}"'+(' aria-current="page"' if key==page else '')+f'>{label}</a>' for key,file,label in [('research','research.html',tr('Research achievements','研究成果')),('projects','projects.html',tr('Projects','项目')),('experience','experience.html',tr('Experience','经历')),('photography','photography.html',tr('Outside work','生活')),('contact','index.html#lei-contact',tr('Contact','联系'))])
    return f'''<!doctype html>
<html lang="{'zh-CN' if lang=='zh' else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#f4f5f2">
<title>{page_title}</title><meta name="description" content="{escape(description)}"><link rel="canonical" href="{BASE+path}">
<link rel="alternate" hreflang="en" href="{BASE+enpath}"><link rel="alternate" hreflang="zh-CN" href="{BASE+'zh/'+enpath}"><link rel="alternate" hreflang="x-default" href="{BASE+enpath}">
<meta property="og:type" content="website"><meta property="og:title" content="{og_title}"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{BASE+path}"><meta property="og:locale" content="{tr('en_GB','zh_CN')}">
<link rel="icon" href="{prefix}assets/icons/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}css/style.css?v=7"><script defer src="{prefix}js/main.js?v=7"></script></head><body>
<a class="skip-link" href="#main">{tr('Skip to content','跳至正文')}</a><header><a class="brand" href="./">{tr('CHENJUN LEI','雷晨俊 / CHENJUN LEI')}</a><nav aria-label="{tr('Main navigation','主导航')}">{nav}<a class="language-switch" data-language-switch href="{other}" lang="{tr('zh-CN','en')}" hreflang="{tr('zh-CN','en')}" aria-label="{tr('切换至中文','Switch to English')}">{tr('中文','EN')}</a></nav></header>
<main id="main">{body}</main><footer><p>© <span data-year>2026</span> CHENJUN LEI</p><p>{tr('May we both have good things to show for it :)','祝我们都有好收获 :)')}</p><a href="#main">{tr('Back to top ↑','回到顶部 ↑')}</a></footer></body></html>'''

def hero(lang,num,title,lead):
    return f'<section class="page-hero"><p class="breadcrumb"><a href="./">{"Home" if lang=="en" else "首页"}</a> / {num}</p><h1>{title}</h1><p class="lead">{lead}</p></section>'

def build(lang):
    tr=lambda a,b:a if lang=='en' else b
    dest=ROOT/('zh' if lang=='zh' else '')
    def save(page,title,desc,body): (dest/(page+'.html')).write_text(render(lang,page,title,desc,body),encoding='utf-8')
    avatar_path='../assets/images/lei-avatar.webp' if lang=='zh' else 'assets/images/lei-avatar.webp'
    avatar_alt=tr('Night hiking in Canberra, with two hikers seen from behind under blue-green light.','堪培拉夜间徒步，两位徒步者的背影映着蓝绿色的夜光。')
    art=f'<figure class="hero-avatar"><img src="{avatar_path}" alt="{avatar_alt}" width="1254" height="1254"></figure>'
    role=tr('Data Engineer at Chuchiang Data in Shanghai and Master of Economics student at the Australian National University. Experienced in data development, FinTech, data-product design and commercialisation, with multiple publications. Interested in automotive modification and classical music; trumpet player in the Australian National University Symphony Orchestra and powertrain assembly engineer with ANUFS Formula Sport.','上海珠江数据工程师，澳大利亚国立大学经济学硕士在读。有丰富的数据开发、金融科技、数据产品设计开发及其商业化经验；拥有多篇论文。热爱汽车改装、古典音乐，现任澳大利亚国立大学交响乐团小号手、ANUFS 方程式赛车队内燃机动力总成工程师。')
    body=f'<section class="hero" id="lei-top"><div><p class="kicker">{tr("Economics / Data / Decisions","经济学 / 数据 / 决策")}</p><h1>{tr("Chenjun Lei.","雷晨俊。")}</h1><p class="intro">{tr("An ordinary enjoyer of life.","一位普通生活享受者。")}</p><p class="role">{role}</p><div class="hero-links">{link("research.html",tr("Research achievements & papers","研究成果与论文"))}{link("experience.html",tr("Experience & education","经历与教育"))}</div></div>{art}</section>'
    body+='<div class="index">'+''.join(f'<a href="#lei-{id}"><span>{n:02} / {label}</span>{title}</a>' for n,(id,label,title) in enumerate([('research',tr('INVESTIGATE','探索'),tr('Research & publications','研究与学术成果')),('projects',tr('BUILD','实践'),tr('Projects & case studies','项目与案例')),('experience',tr('CONTRIBUTE','参与'),tr('Experience & education','工作与教育')),('outside',tr('OBSERVE','观察'),tr('Life beyond work','工作之外'))],1))+'</div>'
    body+='<section class="about-strip"><p class="kicker">'+tr('A little context','关于我')+'</p><p>'+tr('I study economics at the Australian National University and work across financial data, product development and applied research. My experience spans FinTech products at Chuchiang Data, financial audit, debt underwriting and empirical research in Macao.','我在澳大利亚国立大学学习经济学，关注金融数据、产品开发与应用研究。我的经历涵盖珠江数据的金融科技产品、金融审计、债券承销，以及澳门的实证研究。')+'</p></section>'
    body+=chapter('research','01',tr('Research achievements','研究成果'),tr('Questions<br>worth asking.','值得追问<br>的问题。'),''.join(paper(p,lang) for p in papers[:3])+link('research.html',tr('All research & citations','全部研究与引用')))
    cards=''
    for n,p in enumerate(projects):
        cards+=f'<article class="project"><p class="kicker">0{n+1} / {e(p["tag"],lang)}</p><h3>{e(p["title"],lang)}</h3><p>{e(p["intro"],lang)}</p><p class="project-metric">{e(p["metric"],lang)}</p>{link("projects.html#"+p["id"],tr("View project","项目详情"))}</article>'
    portfolio_path='../assets/portfolio/2cases.pdf' if lang=='zh' else 'assets/portfolio/2cases.pdf'
    portfolio=f'<a class="portfolio-feature" href="{portfolio_path}" target="_blank" rel="noopener"><span class="kicker">{tr("Featured work / PDF","精选作品 / PDF")}</span><strong>{tr("Business analysis portfolio","商业分析作品集")}</strong><span>{tr("Two case studies on growth structure and profitability analysis. Open the 19-page portfolio ↗","两份关于增长结构与盈利分析的商业分析案例，点击打开 19 页完整作品集 ↗")}</span></a>'
    body+=chapter('projects','02',tr('Projects','项目'),tr('From ideas<br>to practice.','从想法<br>到实践。'),portfolio+'<div class="project-grid">'+cards+'</div>')
    body+=chapter('experience','03',tr('Experience','经历'),tr('A professional<br>perspective.','在实践中<br>积累视角。'),''.join(job(j,lang) for j in jobs)+link('experience.html',tr('Full experience, education & awards','完整经历、教育与荣誉')))
    body+=chapter('education','04',tr('Education','教育'),tr('Learning<br>with purpose.','持续学习。'),education(lang))
    body+=chapter('outside','05',tr('Outside work','生活'),tr('A different<br>kind of attention.','另一种<br>观察方式。'),photo_carousel(lang, '../' if lang=='zh' else '')+interests(lang, True)+link('photography.html',tr('Beyond the screen','工作之外')))
    contact=f'<h2>{tr("Let’s compare notes.","交换想法，保持联系。")}</h2><p>{tr("Research, data products, or a shared curiosity.","关于研究、数据产品，或一个共同感兴趣的问题。")}</p><dl class="contact-list"><div><dt>{tr("Email","邮箱")}</dt><dd><a href="mailto:fjsmlcj@gmail.com">fjsmlcj@gmail.com</a></dd></div><div><dt>GitHub</dt><dd><a href="https://github.com/Cromwell-Lei">Cromwell-Lei ↗</a></dd></div><div><dt>{tr("Location","所在地")}</dt><dd>{tr("Shanghai, China / Canberra, Australia","中国上海 / 澳大利亚堪培拉")}</dd></div></dl><details class="phone-details"><summary>{tr("Phone contact","电话联系")}</summary><p><a href="tel:+8619168655714">+86 19168655714</a> · <a href="tel:+61458020537">+61 458020537</a></p></details>'
    body+=chapter('contact','06',tr('Contact','联系'),'',contact)
    save('index','ChenjunLei',tr('Chenjun Lei: economics at ANU, FinTech products, synthetic data and applied research. Explore papers, projects, experience and interests.','雷晨俊的个人主页：澳大利亚国立大学经济学、金融科技产品、合成数据与应用研究。论文、项目、工作经历与个人兴趣。'),body)

    body=hero(lang,'01 / '+tr('Research achievements','研究成果'),tr('Questions worth asking.','值得追问的问题。'),tr('Credit risk, safer automated decisions, and the reuse of experience.','信用风险、更安全的自动化决策，以及经验的复用。'))
    body+='<div class="archive-content"><div class="research-overview">'+tr('2026 · 2 accepted conference papers · 1 submitted manuscript<br>2025 · 1 research report','2026 · 2 篇已接收会议论文 · 1 篇投稿论文<br>2025 · 1 项研究报告')+'</div>'+''.join(paper(p,lang,True) for p in papers)+link('projects.html#credit-risk',tr('Explore the credit-risk project','了解信用风险研究项目'))+'</div>'
    save('research',tr('Research & publications','研究与学术成果'),tr('Papers, research summaries, authors, publication status and original sources for Chenjun Lei.','雷晨俊的论文与研究报告：完整作者、投稿状态、研究简介与原文链接。'),body)

    body=hero(lang,'02 / '+tr('Projects','项目'),tr('From ideas to practice.','从想法到实践。'),tr('Financial data products, expert workflows and research-led evaluation.','金融数据产品、专家作业流程，以及研究驱动的模型评估。'))+'<div class="archive-content">'
    for n,p in enumerate(projects):
        body+=f'<section class="archive-block" id="{p["id"]}"><p class="kicker">0{n+1} / {p["date"]} / {e(p["tag"],lang)}</p><h2>{e(p["title"],lang)}</h2><p class="project-metric">{e(p["metric"],lang)}</p><p>{e(p["intro"],lang)}</p><h3 class="contribution-label">{tr("My contribution","我的工作")}</h3>{ul(p["parts"],lang)}'
        if p['id']=='credit-risk': body+=link('research.html#synstress',tr('Related manuscript','相关论文'))
        body+='</section>'
    body+=link('experience.html',tr('Professional experience','工作经历'))+'</div>'
    save('projects',tr('Selected projects','项目经历'),tr('Four projects spanning financial synthetic data, annotation workflows, credit-risk validation and specialist language-model datasets.','金融合成数据、标注平台、信用风险验证与学科大模型数据集四项项目。'),body)

    body=hero(lang,'03 / '+tr('Experience','经历'),tr('Across disciplines.<br>Close to practice.','跨越学科，<br>贴近实践。'),tr('Product development, finance and empirical research — with economics as a common thread.','从产品开发到金融业务与实证研究，以经济学连接不同实践。'))
    body+=chapter('experience','01',tr('Work','工作'),tr('Professional<br>experience.','工作经历。'),''.join(job(j,lang,True) for j in jobs))
    body+=chapter('education','02',tr('Education','教育'),tr('Education.','教育经历。'),education(lang))
    body+=chapter('honors','03',tr('Recognition','荣誉'),tr('Honors &<br>awards.','荣誉与奖励。'),honors(lang))
    body+=chapter('skills','04',tr('Toolkit','技能'),tr('Tools for<br>the work.','方法与工具。'),skills(lang))
    body+=chapter('campus','05',tr('Campus life','校园'),tr('Beyond the<br>classroom.','课堂之外。'),interests(lang))
    body+='<p class="print-control"><button type="button" data-print>'+tr('Print this profile / Save as PDF','打印本页 / 另存为 PDF')+'</button></p>'
    save('experience',tr('Experience & education','经历与教育'),tr('Chenjun Lei’s work experience, education, research-team awards, skills and campus activities.','雷晨俊的工作经历、教育背景、科研团队奖学金、技能与校园活动。'),body)

    body=hero(lang,'04 / '+tr('Outside work','生活'),tr('A different kind<br>of attention.','另一种<br>观察方式。'),tr('Photography, music and the mechanics of things that move.','摄影、音乐，以及驱动车辆前行的机械。'))
    body+='<section class="archive-block">'+interests(lang, True)+'</section><section class="photobook-note" id="photobook"><p class="kicker">'+tr('Personal photobook / In development','个人影集 / 筹备中')+'</p><h2>世界皆舞台</h2><p>'+tr('All the World’s a Stage','用影像，记录我所看见的世界。')+'</p>'+photo_carousel(lang, '../')+'<p class="archive-note">'+tr('A photographic collection in preparation. Selected photographs will be added as the sequence takes shape.','正在整理与编排中的个人摄影作品集。精选作品将在编排成形后陆续加入。')+'</p></section>'+link('index.html#lei-contact',tr('Get in touch','保持联系'))
    save('photography',tr('Outside work','工作之外'),tr('Photography, trumpet and Formula Sport: Chenjun Lei beyond research and work.','摄影、小号与方程式赛车：研究和工作之外的雷晨俊。'),body)

for lang in ('en','zh'): build(lang)
urls=[BASE+prefix+('' if p=='index' else p+'.html') for prefix in ('','zh/') for p in ('index','research','projects','experience','photography')]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>\n')
for p in papers:
    if 'arxiv' not in p: continue
    bib='@misc{'+p['id'].replace('-','')+'2026,\n  title = {'+p['title']+'},\n  author = {'+' and '.join(p['authors'].split(', '))+'},\n  year = {2026},\n  eprint = {'+p['arxiv']+'},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n  doi = {10.48550/arXiv.'+p['arxiv']+'},\n  url = {https://arxiv.org/abs/'+p['arxiv']+'}\n}\n'
    (ROOT/'assets/citations'/(p['id']+'.bib')).write_text(bib)
