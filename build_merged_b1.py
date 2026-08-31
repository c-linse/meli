# -*- coding: utf-8 -*-
"""Build merged Part B-1 (B1_red_revisions.md applied to the original text),
render to PDF via LibreOffice, then append the original Part B-2 pages (9-11)."""
import subprocess, os, base64, pymupdf
from PIL import Image, ImageDraw, ImageFont

def make_gantt(path):
    SANS  = "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf"
    SANSB = "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf"
    f_lbl = ImageFont.truetype(SANS, 26)
    f_hdr = ImageFont.truetype(SANSB, 24)
    f_ms  = ImageFont.truetype(SANSB, 22)
    LBLW, CW, HDRH, ROWH = 620, 46, 42, 52
    x0 = 20 + LBLW
    rows = [
      ("T1.1  Plastochron & phyllotaxis vs thermal time", (169,200,232), 1, 8),
      ("T1.2  Live imaging of reporters (CherryTemp)",     (169,200,232), 3, 12),
      ("T2.1  Redox compartmentalisation vs temperature",  (183,215,168), 4, 12),
      ("T2.2  NO transducer: donors/scavengers, mutants",  (183,215,168), 6, 20),
      ("T3.1  Factorial snRNA-seq (with Reis, U Bern)",    (245,195,150), 8, 16),
      ("T3.2  Analysis & candidate gene networks",         (245,195,150), 14, 22),
      ("T4.1  Management, supervision, DMP & CDP",          (204,204,204), 1, 24),
      ("T5.1  Conferences and seminars",                    (217,179,208), 1, 24),
      ("T5.2  Public engagement / outreach",                (217,179,208), 4, 24),
      ("T5.3  Manuscript 1 (WP1+WP2)",                      (217,179,208), 16, 22),
      ("T5.4  Manuscript 2 (WP3)",                          (217,179,208), 21, 24),
      ("Long-lead: mutant x reporter crosses",              (221,221,221), 1, 6),
    ]
    mstones = {6: "M1", 18: "M2", 22: "M3"}
    W = x0 + 24*CW + 14
    H = HDRH + (len(rows)+1)*ROWH + 8
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    for m in range(25):
        gx = x0 + m*CW
        d.line([(gx, HDRH-4), (gx, H-8)], fill=(210,210,210), width=1)
    for m in range(1, 25):
        d.text((x0 + (m-0.5)*CW, HDRH/2), str(m), font=f_hdr, fill=(60,60,60), anchor="mm")
    d.line([(0, HDRH-4), (W, HDRH-4)], fill=(120,120,120), width=1)
    for i, (lbl, col, s, e) in enumerate(rows):
        ry = HDRH + i*ROWH
        d.text((20, ry + ROWH/2), lbl, font=f_lbl, fill=(20,20,20), anchor="lm")
        bx0, bx1 = x0 + (s-1)*CW, x0 + e*CW
        d.rectangle([bx0+1, ry+5, bx1-1, ry+ROWH-5], fill=col, outline=(150,150,150))
    my = HDRH + len(rows)*ROWH
    d.text((20, my + ROWH/2), "Milestones (M1-M3)", font=f_ms, fill=(20,20,20), anchor="lm")
    for m, name in mstones.items():
        cx, cy, r = x0 + (m-0.5)*CW, my + ROWH/2, 7
        d.polygon([(cx, cy-r), (cx+r, cy), (cx, cy+r), (cx-r, cy)], fill=(30,30,30))
        d.text((cx, cy - r - 9), name, font=f_ms, fill=(20,20,20), anchor="mm")
    im.save(path, "PNG")
    return path

OUT_DIR = "/tmp/claude-1000/-home-clinse-dev-meli/76931ef6-3fa6-4b72-825b-60ff15571ac3/scratchpad"
ORIG = "/home/clinse/dev/meli/Luquet Melisa section B1 revised.pdf"
FINAL = "/home/clinse/dev/meli/Luquet Melisa section B1 MERISTIME.pdf"

CSS = """
@page { size: A4; margin: 1.4cm 1.9cm; }
body { font-family: 'Times New Roman', serif; font-size: 11pt; line-height: 1.13;
       text-align: justify; color: #000; }
h1 { font-size: 12.5pt; color: #0f4761; margin: 12pt 0 4pt; }
h2 { font-size: 11pt; font-style: italic; margin: 9pt 0 3pt; }
p  { margin: 0 0 5pt; }
.title { text-align: center; font-weight: bold; font-size: 11.5pt; margin: 5pt 0 8pt; }
.hdr { font-size: 9pt; color: #555; text-align: center; margin: 0 0 3pt; }
.runin { font-weight: bold; }
.refs { font-size: 9pt; line-height: 1.15; }
.refs p { margin: 0 0 1pt; }
.rule { text-align: center; color: #555; font-size: 9pt; margin: 8pt 0; }
.caption { font-weight: bold; font-size: 9pt; margin: 7pt 0 2pt; }
.legend { font-size: 8pt; color: #444; margin: 0 0 6pt; }
img.gantt { width: 100%; margin: 2pt 0 2pt; }
table.tbl { border-collapse: collapse; width: 100%; font-size: 8pt; margin: 2pt 0 7pt; line-height: 1.12; }
table.tbl th, table.tbl td { border: 0.5px solid #999; padding: 2px 4px; text-align: left; vertical-align: top; }
table.tbl th { background: #eeeeee; }
table.tbl td.c { text-align: center; }
"""

def P(runin, rest=""):
    if runin and rest:
        return f'<p><span class="runin">{runin}</span> {rest}</p>'
    if runin:
        return f'<p><span class="runin">{runin}</span></p>'
    return f'<p>{rest}</p>'

blocks = []
A = blocks.append

A('<p class="hdr">Call: HORIZON-MSCA-2025-PF &mdash; MERISTIME</p>')
A('<h1 style="text-align:center;color:#000;font-size:13pt;">Part B-1</h1>')
A('<h1>1. Excellence</h1>')
A('<h2>1.1&nbsp;&nbsp;Quality and pertinence of the project&rsquo;s research and innovation objectives '
  '(and the extent to which they are ambitious, and go beyond the state of the art)</h2>')
A('<p class="title">MERISTIME &mdash; From thermosensing to organ timing in the shoot apical meristem</p>')

A(P('Introduction.'))
A(P('', 'Unlike animals, whose body plan is essentially fixed during embryogenesis, plants build most of '
     'their body after germination. This post-embryonic mode of development is the source of their '
     'remarkable plasticity, and it depends on the sustained activity of meristems, a specific tissue '
     'containing stem cells that give rise to all plant organs.'))
A(P('', 'The shoot apical meristem (SAM) originates all aerial organs leading to the initiation of leaves, '
     'stems and flowers; during vegetative development, its activity sets the pace for leaf initiation '
     'rate, known as the <span class="runin" style="font-weight:bold">plastochron</span>. Temperature is a '
     'central regulator of this rate: within a biologic range, warmer temperature accelerates leaf '
     'production, and this acceleration is so regular that the rate of leaf initiation is linearly related '
     'to thermal time &mdash; the number of degree-days the plant experiences over a given period. This '
     'relationship is conserved from Arabidopsis to crops and is a major determinant of development and '
     'yield. While temperature signaling has been dissected in detail in the context of hypocotyl '
     'elongation, its action within the SAM, where the organs that shape the plant are born, '
     '<b>remains almost completely unexplored</b>. This project aims to decipher how the SAM perceives and '
     'transduces temperature cues to set the plastochron and proposes that a missing piece might be the '
     'redox and nitric oxide (NO) signaling.'))

A(P('State of the art and objectives.'))
A(P('', 'The SAM is organized into functional zones. In the central zone, a WUSCHEL (WUS)&ndash;CLAVATA3 '
     '(CLV3) feedback loop maintains stem cell identity; in the peripheral zone, faster-dividing cells '
     'differentiate into leaf primordia at sites specified by PIN1-dependent auxin maxima, with cytokinin '
     'promoting leaf proliferation. Recent 3D imaging showed that temperature acts directly within the '
     'SAM, altering meristem size and WUS/CLV3 expression patterns<sup>1</sup>. However, <b>how these '
     'changes drive leaf initiation, whether temperature signals through auxin or cytokinin pathways, and '
     'how temperature perception is first transduced into SAM activity remain unknown.</b>'))
A(P('', 'Temperature-sensing has been described in the hypocotyl: phytochrome B (phyB) acts as a '
     'thermosensor inactivated at warm temperature<sup>4</sup>; ELF3, a transcriptional regulator, also '
     'gets inactivated under warm temperature; PIF7 whose transcription increases through '
     'temperature-dependent mRNA translation; and warm temperature drives starch breakdown and sucrose '
     'production. Downstream, signalling converges on PIF4 and the E3 ligase COP1<sup>5</sup>. Whether '
     'these mechanisms also operate in the SAM to control leaf initiation is unknown.'))
A(P('', 'In parallel, it is known that redox species constitutes key signals within the SAM. The meristem '
     'is also redox-compartmentalised: superoxide accumulates in the central zone, sustaining WUS and '
     'stemness, whereas hydrogen peroxide and NO are enriched in the differentiating peripheral zone, and '
     'disrupting this gradient reduces SAM size and delays early leaf development<sup>2&ndash;3</sup>. The '
     'peripheral zone is precisely where primordia are initiated, so the NO-rich domain coincides with the '
     'site where the plastochron is literally set. NO promotes peripheral-zone fate by repressing WUS, in '
     'part by limiting the stem-cell regulator AGO4 to the centre through S-nitrosylation, with WUS '
     'interacting with AGO4 in a NO-dependent manner<sup>3</sup>.'))

A(P('Preliminary results.'))
A(P('', 'Using a thermal-time phenotyping assay restricted to the vegetative phase, I have compared wild '
     'type and the thermosensor mutant phyB across temperatures. Wild type holds the plastochron on an '
     'essentially constant thermal-time relationship, whereas phyB does not: its leaf-initiation rate '
     'departs from the thermal-time expectation (Fig. 1). This identifies a meristem-level temperature '
     'phenotype for phyB, distinct from its established role in hypocotyl elongation, and it is the '
     'observation on which the project is built. I have also begun to manipulate NO in the apex with the '
     'donor GSNO and the scavenger cPTIO, read on the same thermal-time basis; these experiments are in '
     'progress and have not yet produced a clear plastochron phenotype, and establishing whether NO acts '
     'downstream of temperature in the meristem is the central question of WP2. The reporter lines (pCLV3, '
     'pWUS, DR5, PIN1) and the CherryTemp-based live-imaging required for WP1 are in place in the host '
     'laboratory.'))
A('<p style="color:#666"><i>[Figure 1 &mdash; to be supplied by the applicant: plastochron vs thermal '
  'time, wild type vs phyB.]</i></p>')

A(P('Hypothesis and objectives.',
    'My hypothesis is that temperature is transduced in the SAM through a redox/NO node that remodels the '
    'peripheral-zone redox landscape to set the plastochron. <b>The general aim is to understand the early '
    'mechanisms linking temperature perception to plastochron regulation in the SAM.</b>'))
A(P('WP1: Characterisation of the temperature response of the meristem during early development.',
    'I aim to describe the effect of temperature on SAM function and leaf initiation with high spatial and '
    'temporal resolution (plastochron on thermal-time basis, SAM size, WUS/CLV3 expression and '
    'distribution).'))
A(P('WP2: Role of phyB and of redox/NO signalling in the temperature control of leaf initiation.',
    'I will test whether the canonical thermosensor phyB and the meristem redox/NO system transduce '
    'temperature into plastochron regulation. Task 2.1 addresses the general redox state of the meristem '
    '&mdash; the superoxide/H&#8322;O&#8322; balance across the central and peripheral zones &mdash; as a '
    'function of temperature; Task 2.2 addresses nitric oxide specifically, through in vivo detection, NO '
    'donors and scavengers, and NO-pathway mutants, asking whether NO perturbation reproduces the phyB '
    'phenotype established in my preliminary work.'))
A(P('WP3: Single-cell transcriptomic response of the SAM to warm temperature.',
    'Using a factorial temperature &times; thermal-time design, I will characterise the meristem&rsquo;s '
    'temperature response at cellular resolution and test whether known meristem regulators &mdash; the '
    'WUS/CLV3 network, zonal redox and NO-biosynthesis genes, and auxin readouts &mdash; participate in '
    'temperature and thermal-time sensing. This yields the temperature- and redox-responsive gene networks '
    'of the SAM and a reusable community dataset, and is carried out with R. Reis (University of Bern).'))
A(P('Originality and ambition.',
    'Three features make the project original. First, it moves temperature signalling out of the '
    'hypocotyl, where it is almost exclusively studied, and into the shoot apical meristem, where the '
    'organs that shape the plant are initiated. Second, it proposes a specific, testable transducer &mdash; '
    'a redox/NO node in the peripheral zone &mdash; rather than treating meristem thermosensing as a '
    'generic unknown: my preliminary data establish that phyB is required to hold the plastochron on a '
    'constant thermal-time relationship, a meristem phenotype distinct from the canonical '
    'hypocotyl-elongation output, and I propose that phyB acts here through a redox/NO route rather than '
    'the PIF4/COP1 growth-effector branch. Third, it connects two fields that have developed in parallel '
    '&mdash; thermomorphogenesis, which has identified the sensors, and the redox biology of the stem-cell '
    'niche, which provides the positional signals that pattern organ initiation. Establishing how an '
    'environmental cue is converted into the timing of organ formation is of broad significance for '
    'developmental biology and directly relevant to crop resilience under a warming climate, where the '
    'rate of leaf initiation shapes canopy establishment and yield.'))

A('<h2>1.2&nbsp;&nbsp;Soundness of the proposed methodology (including interdisciplinary approaches, '
  'consideration of the gender dimension and other diversity aspects if relevant for the research project, '
  'and the quality of open science practices)</h2>')
A(P('Overall approach.',
    'The methodology pairs two logics rarely combined in one laboratory: the quantitative, imaging-based '
    'developmental biology of the shoot apical meristem, and the biochemistry of nitric oxide and redox '
    'signalling. A single output &mdash; the rate and pattern of organ initiation, expressed on a '
    'thermal-time basis &mdash; is read through three complementary lenses (genetic and phenotypic, in '
    'vivo imaging, and biochemical), so that no central claim rests on one technique. All experiments are '
    'restricted to the vegetative phase and controlled for flowering time, and thermal time is computed '
    'from logged growth-chamber temperatures, so that chronological age and developmental progression are '
    'separated throughout.'))
A(P('WP1 &mdash; Characterisation of the temperature response of the meristem during early development.'))
A(P('Task 1.1 &mdash; Plastochron and phyllotaxis against thermal time.',
    'I will quantify the plastochron and the phyllotactic divergence angle in wild type and selected '
    'mutants (phyB and the NO-pathway mutants used in WP2), grown at contrasting constant temperatures and '
    'under defined temperature shifts. Per-genotype linear models of leaf number against thermal time are '
    'compared statistically to establish whether each genotype maintains a constant thermal-time '
    'relationship (compensation) or departs from it.'))
A(P('Task 1.2 &mdash; Live imaging of meristem and auxin reporters under controlled temperature.',
    'Using the stem-cell reporters pCLV3 and pWUS and the auxin reporters DR5 and PIN1, I will image the '
    'living apex by confocal microscopy on the spectral confocal microscope recently acquired by the '
    'Institute of Biology (SNSF R&rsquo;equip, 2024), with temperature controlled at the sample by the '
    'CherryTemp system available in the host laboratory (stable set-points and rapid shifts during '
    'time-lapse). Readouts &mdash; SAM size, the size and position of the WUS and CLV3 domains, the '
    'position of PIN1-dependent auxin maxima, and the timing of primordium emergence &mdash; are each '
    'placed on a thermal-time axis.'))
A(P('WP2 &mdash; Role of phyB and of redox/NO signalling in the temperature control of leaf initiation.'))
A(P('Task 2.1 &mdash; Temperature and the redox compartmentalisation of the meristem.',
    'I will map reactive redox species in the living apex across temperatures and in phyB: the '
    'superoxide/hydrogen peroxide balance (DHE and NBT for O&#8322;&#183;&#8315;; H&#8322;DCFDA and DAB for '
    'H&#8322;O&#8322;), quantified by confocal imaging and histochemistry. The question is whether warm '
    'temperature reconfigures the central-versus-peripheral redox pattern described by Zeng et '
    'al.<sup>2&ndash;3</sup>, and whether any such change depends on phyB.'))
A(P('Task 2.2 &mdash; Nitric oxide as a candidate temperature transducer.',
    'NO is detected in vivo with DAF-FM DA and perturbed genetically (gsnor1/hot5, nia1&nbsp;nia2, noa1) '
    'and pharmacologically (the donor GSNO and the scavenger cPTIO; glutathione as a control for the '
    'general thiol-redox context, not as an NO-specific treatment). All perturbations are read on a '
    'thermal-time basis and compared directly with the phyB phenotype. My preliminary data establish that '
    'phyB fails to hold the plastochron on a constant thermal-time relationship; NO manipulations are in '
    'progress and have not yet produced a clear phenotype. The decisive experiment of this task is whether '
    'NO perturbation reproduces this loss of thermal-time compensation. NO-pathway mutants are crossed '
    'with the DR5, PIN1, WUS and CLV3 reporters to localise any effect within the meristem, and candidate '
    'S-nitrosylation targets in the stem-cell niche (e.g. AGO4) are probed by biotin-switch assays.'))
A(P('WP3 &mdash; Single-cell transcriptomic response of the SAM to warm temperature.'))
A(P('', 'Comparing two temperatures at equal chronological age confounds temperature with developmental '
     'stage (warm develops faster); comparing at equal thermal time controls development but not '
     'chronological age.'))
A(P('Task 3.1 &mdash; Factorial temperature &times; thermal-time design.',
    'I will profile dissected vegetative apices by single-nucleus RNA-seq under a factorial design: two '
    'temperatures (control vs warm) &times; two matched thermal-time points, rather than a gradient, which '
    'for single-cell work would dilute replication and power. This separates the effect of temperature at '
    'matched development from the effect of developmental progression and provides a direct test of '
    'compensation: a gene genuinely compensated on a thermal-time basis should not differ between '
    'temperatures once thermal time is matched.'))
A(P('Task 3.2 &mdash; Analysis and candidate networks.',
    'Predictions from Zeng et al.<sup>2&ndash;3</sup> anchor quality control and a targeted analysis '
    'panel: WUS/CLV3 targets, AGO4 and RdDM components, zonal ROS-metabolising enzymes, the NO-biosynthesis '
    'genes NIA1, NIA2 and NOA1, and auxin readouts. Library preparation and single-cell analysis are '
    'carried out in collaboration with R. Reis (University of Bern), who provides the single-cell '
    'transcriptomics expertise; short technical visits to Bern are foreseen for the wet-lab and '
    'computational steps.'))
A(P('Interdisciplinarity.',
    'The project sits at the interface of developmental biology, plant physiology and redox biochemistry. '
    'Its feasibility rests on combining expertise that does not currently coexist in one place: the '
    'host&rsquo;s developmental and photobiological framework and quantitative live-imaging, my own '
    'redox/NO biochemistry and in vivo detection, and the single-cell transcriptomics of the Reis group.'))
A(P('Open science.',
    'Data are managed under a FAIR-compliant Data Management Plan prepared in the first months and updated '
    'thereafter. Datasets underlying publications &mdash; imaging, quantitative phenotyping and the '
    'single-nucleus dataset &mdash; are deposited in recognised community repositories with persistent '
    'identifiers. Publications are made immediately open access and deposited in Libra, the institutional '
    'repository of the University of Neuch&acirc;tel, with preprints posted at submission. Protocols and '
    'analysis code, including the thermal-time image-analysis and statistical pipelines, are shared '
    'openly, and confirmatory analyses are pre-registered where possible.'))
A(P('Sex and gender dimension.',
    'This project is performed in the plant <i>Arabidopsis thaliana</i>, so a sex and gender dimension '
    'does not apply to its research methodology; however, gender dimension is considered.'))

A('<h2>1.3&nbsp;&nbsp;Quality of the supervision, training and of the two-way transfer of knowledge '
  'between the researcher and the host</h2>')
A(P('What I gain from the host.',
    'My doctoral training in Argentina was in NO and redox signalling in plant physiology, at the level of '
    'the whole plant and of biochemical readouts. This fellowship provides what I do not yet have: the '
    'capacity to ask developmental questions at cellular resolution and in real time. This research group '
    'works at the interface of light and temperature signalling and shoot development, making it the '
    'environment where I can convert my signalling expertise into developmental biology. My training plan '
    'centres on three scientific competences the project requires and that I do not yet have: quantitative '
    'live-imaging of the meristem (reporter lines, temperature-controlled imaging with CherryTemp, 3D '
    'image-analysis pipelines); the genetics and conceptual framework of thermomorphogenesis, a field to '
    'which my supervisor is a foundational contributor; and single-nucleus transcriptomics together with '
    'its computational analysis. Technical training is provided within the host group and, for the '
    'single-cell work, through the collaboration with R. Reis (Bern) and dedicated courses of the Swiss '
    'Institute of Bioinformatics (bulk and single-cell RNA-seq analysis). Transferable-skills and career '
    'training is provided by the UniNE Graduate Campus (part of the swissuniversities 2025&ndash;2028 '
    'programme for the promotion of academic talent) and by the doctoral programmes of UniNE and the CUSO; '
    'I will also attend the EMBO Laboratory Leadership for Postdocs course and present at international '
    'plant photobiology and thermomorphogenesis meetings, including those co-organised by my supervisor in '
    '2026.'))
A(P('What I bring to the host.',
    'The host group has no in vivo redox capability. I bring the detection of reactive redox species in '
    'living tissue (DAF-FM DA for NO; H&#8322;DCFDA and DHE for ROS), the genetics of NO homeostasis, the '
    'pharmacological manipulation of NO with donors and scavengers, and the biochemistry of cysteine-based '
    'post-translational modifications, including biotin-switch workflows. The group&rsquo;s interest in '
    'redox as an integrator of environmental and endogenous cues in the meristem is explicit and current '
    '&mdash; for example in the shade-induced ROS/NO work my supervisor co-authored<sup>7</sup> &mdash; '
    'but the technical capacity to pursue it in vivo is not yet established in Neuch&acirc;tel. My arrival '
    'makes that line executable and installs a capability that will outlive the fellowship: a genuine '
    'two-way transfer of knowledge.'))
A(P('Quality of supervision.',
    'Prof. Martina Legris leads a research group at the Institute of Biology, University of Neuch&acirc;tel. '
    'She specialises in the molecular signalling of photoreceptors and in developmental plasticity in '
    'response to light and temperature, with over 20 publications including first- or corresponding-author '
    'papers in <i>Science</i>, <i>PNAS</i>, <i>Nature Communications</i>, <i>New Phytologist</i> and '
    '<i>Plant Physiology</i>, and she received the 2023 <i>New Phytologist</i> Tansley Medal. Her '
    'contribution is foundational: she is first author of the work establishing phyB as a thermosensor '
    'that integrates light and temperature in Arabidopsis<sup>4</sup>, and she has since developed the '
    'study of light and temperature control of leaf and meristem morphogenesis<sup>5&ndash;7</sup>. She '
    'trained in the Casal and Fankhauser laboratories and is herself a former MSCA, EMBO and HFSP fellow, '
    'so she knows the fellowship from the inside. My project is a direct extension of a question her own '
    'work opened &mdash; how temperature is read in the meristem to set leaf initiation &mdash; which '
    'makes the supervision scientifically substantive.'))
A(P('', 'The group comprises the supervisor, one postdoctoral researcher and one PhD student, with a '
     'second postdoc (myself) joining on this project; the supervisor has additionally mentored numerous '
     'master&rsquo;s and summer students. It is funded by an SNSF Starting Grant (TMSGI3_218178, '
     '&ldquo;Environmental control of shoot architecture in Arabidopsis&rdquo;, 2023&ndash;2028) and by a '
     'two-year Fondation Mercier pour la Science grant (&ldquo;Temperature regulation of leaf initiation '
     'in Arabidopsis thaliana&rdquo;, 2026) that establishes the research line this fellowship contributes '
     'to, with access to a spectral confocal microscope co-funded by the supervisor (SNSF R&rsquo;equip, '
     '2024). Supervision is organised around weekly one-to-one and group meetings, a Career Development '
     'Plan agreed in the first months and reviewed at regular intervals, and quarterly progress '
     'presentations. In the second year I will co-supervise, with the supervisor&rsquo;s support, a '
     'master&rsquo;s student on a defined part of the project.'))
A(P('Secondment.',
    'No secondment is foreseen. The single-nucleus transcriptomics of WP3 is carried out through a '
    'scientific collaboration with the group of Dr R. Reis (University of Bern), involving short technical '
    'visits rather than a formal secondment.'))

A('<h2>1.4&nbsp;&nbsp;Quality and appropriateness of the researcher&rsquo;s professional experience, '
  'competences and skills</h2>')
A(P('', 'I obtained my PhD in Exact Sciences (Biological Sciences and Biotechnology) with special '
     'distinction from the National University of La Plata in 2025, at the Institute of Plant Physiology '
     '(INFIVE, UNLP-CONICET), on the role of NO in acclimation to phosphorus restriction. I established '
     'that nitrate reductase mediates NO generation and that this NO is required for acclimation '
     'responses, published as first author<sup>8</sup>, and contributed to five further papers including '
     'reviews that helped define the agenda linking NO signalling to nutrient use efficiency. My work '
     'received the Best Poster Prize at the XXXV Meeting of the Argentine Society of Plant Physiology '
     '(2025) and I was awarded a competitive travel grant to present the flash talk &ldquo;At the apex of '
     'thermomorphogenesis&rdquo; at the 2026 thermomorphogenesis meeting in Dundee, which reflects the '
     'reception of this new line of work by the very community this project addresses.'))
A(P('', 'I bring to the lab first, technical skills built by necessity: I established and applied in vivo '
     'redox imaging, enzymatic and HPLC determinations, biochemical analysis and hydroponic physiology, in '
     'a setting where techniques are more often built than bought. Second, early independence: I supervised '
     'an undergraduate project student for three years, taught as a teaching assistant, and sought out '
     'collaborations of my own, including with Lamattina&rsquo;s group in Mar del Plata (2021), which '
     'resulted in a co-authored paper<sup>9</sup>, and a research stay in the Chromosome Dynamics group at '
     'IPS2, Universit&eacute; Paris-Saclay (2025), whose expertise in chromatin biology and DNA '
     'methylation connects directly to the AGO4/RdDM dimension of the redox&ndash;meristem link addressed '
     'in WP2 and WP3. Third, sustained science outreach, which I will continue in Neuch&acirc;tel.'))
A(P('', 'My doctorate gave me a clear identity as a redox biologist, and this fellowship is the moment to '
     'put that identity to work on questions I could not ask alone. Moving into developmental biology is a '
     'deliberate choice: redox signalling is already recognised as a regulator of meristem activity, but '
     'the tools to follow it in vivo and to connect it to temperature are not established there, and that '
     'is what I bring. Throughout my training in Argentina and in France I learned that science moves '
     'through people, and that open, collaborative practice is what makes knowledge grow. That is why I '
     'share materials and protocols openly and invest time in outreach, and why I intend to publish this '
     'project&rsquo;s results in open access and to deposit its data and protocols in public repositories. '
     'My long-term objective is to lead an independent group on how environmental signals are transduced '
     'by redox chemistry into developmental decisions.'))

A('<h1>2. Impact</h1>')
A('<h2>2.1&nbsp;&nbsp;Credibility of the measures to enhance the career perspectives and employability of '
  'the researcher and contribution to their skills development</h2>')
A(P('', 'My long-term objective is to lead an independent research group at the interface of redox biology '
     'and plant development. This fellowship is the decisive step towards that goal: it adds to my '
     'established expertise in nitric oxide and redox physiology the three competences this research '
     'programme requires and that I currently lack &mdash; quantitative live-imaging of development at '
     'cellular resolution, the genetics and conceptual framework of thermomorphogenesis, and single-cell '
     'transcriptomics with its computational analysis. Acquiring these in a group working at the interface '
     'of light, temperature and shoot development positions me to lead a distinctive line of research that '
     'few others can, precisely because it joins two communities that rarely meet.'))
A(P('', 'My skills development is organised around a Career Development Plan, agreed with my supervisor in '
     'the first months of the fellowship and reviewed at regular intervals, which sets objectives for '
     'research training, transferable skills and career progression. Scientific training follows the work '
     'packages: WP1 and WP2 build my competence in reporter-based confocal imaging, temperature-controlled '
     'live-imaging and image quantification, while WP3, with the Reis group in Bern, introduces me to '
     'single-nucleus transcriptomics and the bioinformatic analysis of complex datasets, an increasingly '
     'indispensable skill in plant developmental biology.'))
A(P('', 'Transferable skills are supported by the host institution. The UniNE Graduate Campus, established '
     'under the swissuniversities 2025&ndash;2028 programme for the promotion of academic talent, offers '
     'workshops and courses for the career development of postdoctoral researchers, and I will also have '
     'access, subject to availability, to courses of the doctoral programmes of UniNE and the CUSO. I will '
     'use this provision to strengthen the competences an independent researcher needs beyond the bench: '
     'scientific writing and grant preparation, project and data management, research integrity, and '
     'leadership and supervision &mdash; the last supported by the EMBO Laboratory Leadership for Postdocs '
     'course. I will further participate in the R&eacute;seau romand de mentorat pour femmes and the '
     'REGARD workshop programme, which support the progression of women towards independent academic '
     'positions.'))
A(P('', 'Supervision experience is a deliberate part of the plan: in the second year I will propose and '
     'co-supervise a master&rsquo;s student on a defined part of the project, with my supervisor&rsquo;s '
     'support, gaining first-hand experience of mentoring and of scoping a project for a student. Together '
     'with the teaching experience I bring from Argentina, this prepares me for the training '
     'responsibilities of a group leader.'))
A(P('', 'Finally, the fellowship substantially widens my network. Beyond the host group, '
     'Switzerland&rsquo;s position and my supervisor&rsquo;s collaborations give me access to the European '
     'plant-science community, and I will present my results at international conferences &mdash; the '
     'International Conference on Arabidopsis Research (ICAR), the EPSO Plant Biology Europe congress, and '
     'thermomorphogenesis and plant-development meetings &mdash; and at institutional seminars. Combined '
     'with my international trajectory across Argentina, France and Switzerland, and a portfolio that will '
     'by then span redox biochemistry, developmental imaging and single-cell genomics, this makes me '
     'competitive for independent-investigator schemes such as the SNSF Ambizione and Starting Grants and '
     'the ERC Starting Grant, whether I continue in Europe or return to Latin America, where these '
     'competences are scarce.'))

A('<h2>2.2&nbsp;&nbsp;Suitability and quality of the measures to maximise expected outcomes and impacts, '
  'as set out in the dissemination and exploitation plan, including communication activities</h2>')
A(P('Dissemination.',
    'The primary route for disseminating results is peer-reviewed publication. I anticipate at least two '
    'papers: a first on the characterisation of the temperature response of the SAM (WP1) together with '
    'the redox and NO perturbation experiments (WP2), and a second built on the single-nucleus dataset '
    '(WP3). Because the project sits at the intersection of two communities, I will target journals read '
    'by both plant developmental biologists and the environmental-signalling and redox fields, and I will '
    'post preprints at the time of submission so that results reach both communities without delay. I will '
    'publish open access and deposit the accepted versions in Libra, the institutional open-access '
    'repository of the University of Neuch&acirc;tel, in compliance with Horizon Europe requirements.'))
A(P('', 'Results will also be disseminated at the international conferences listed in section 2.1 and at '
     'specialised meristem-biology meetings, through seminars at UniNE and partner institutions, and '
     'through the collaboration with the Reis group. Presenting to audiences of different composition, '
     'from a specialised meristem-biology audience to a broader plant-science one, is itself part of my '
     'training in scientific communication.'))
A(P('', 'Research data are a deliverable in their own right. All data underlying publications &mdash; '
     'imaging data, quantitative phenotyping datasets and the single-nucleus transcriptomic dataset '
     '&mdash; will be managed under a Data Management Plan following the FAIR principles and deposited in '
     'recognised community repositories with persistent identifiers. The single-nucleus dataset of the SAM '
     'temperature response (WP3) is designed as a reusable community resource: there are few single-cell '
     'datasets of the vegetative shoot apex and none, to my knowledge, addressing temperature, so its '
     'value extends well beyond the questions I ask of it here. Protocols and analysis code, including the '
     'thermal-time quantification and image-analysis pipelines, will be shared openly so that the methods '
     'are reusable.'))
A(P('Exploitation.',
    'The project is basic research and no intellectual property is anticipated at the outset. However, '
    'leaf-initiation rate is a determinant of canopy establishment and yield, and identifying redox-based '
    'mechanisms that set it could open routes to modulate meristem activity, whether through breeding '
    'targets or through chemical modulation of redox signalling. Should an exploitable result emerge, I '
    'will assess it with my supervisor and with the research and technology-transfer services of the '
    'University of Neuch&acirc;tel, and any decision on protection will be taken before publication.'))
A(P('Communication.',
    'Communication activities are distinct from dissemination and are directed at audiences beyond the '
    'scientific community. I have a sustained record of public engagement &mdash; Fascination of Plants '
    'Day, university science festivals and open-science advocacy in Argentina &mdash; and I will continue '
    'this in Neuch&acirc;tel through the university&rsquo;s public-engagement programme <span '
    'style="color:#666">[specify local formats, e.g. Jardin botanique de Neuch&acirc;tel, Fascination of '
    'Plants Day, Pint of Science]</span>. The message I will build for general audiences connects the '
    'project to something tangible: how plants decide when to make a leaf, and why that decision matters '
    'as temperatures rise. I will also contribute to institutional communication channels and press '
    'releases where results warrant it, and use social media to reach the wider plant-science and student '
    'community. As a woman researcher trained in Latin America and working in Europe, I see value in '
    'making that trajectory visible to students considering research careers, and I will seek '
    'opportunities to do so.'))

A('<h2>2.3&nbsp;&nbsp;The magnitude and importance of the project&rsquo;s contribution to the expected '
  'scientific, societal and economic impacts</h2>')
A(P('Scientific impact.',
    'The project addresses a gap that is conspicuous once stated: temperature is one of the strongest '
    'environmental regulators of plant form, and the shoot apical meristem is where plant form originates, '
    'yet the mechanisms linking the two are essentially unknown. Almost everything known about plant '
    'thermosensing comes from the hypocotyl, a tissue whose response is driven by cell expansion. By '
    'asking the same question in the meristem, where the relevant processes are stem-cell homeostasis, '
    'cell division and differentiation, the project tests whether the established thermosensory framework '
    'generalises or whether the meristem uses a different logic; my preliminary data point to the latter, '
    'which would be a substantive contribution in itself. Beyond this, the project brings redox and nitric '
    'oxide signalling into contact with thermomorphogenesis, two fields that have developed largely in '
    'parallel, and delivers a single-nucleus dataset of the temperature response of the shoot apex that '
    'will serve as a community resource. Because few groups work on the environmental regulation of '
    'meristem activity, and because I will work at the interface of the developmental and '
    'temperature-signalling communities, I expect the results to be of broad interest across plant '
    'biology.'))
A(P('Societal impact.',
    'The rate at which leaves are produced determines how quickly a canopy is established, and canopy '
    'establishment governs light capture, water use and ultimately yield. This relationship is conserved '
    'from Arabidopsis to crops such as rice and maize. Under climate change, with rising mean temperatures '
    'and more frequent warm episodes, the temperature dependence of leaf initiation becomes directly '
    'relevant to how crops perform in the field. Understanding the mechanism that sets this rate is a '
    'prerequisite for any strategy that seeks to adjust it, and contributes to the broader European '
    'objectives of climate-resilient and sustainable agriculture and of food security. The project also '
    'contributes to society through training &mdash; it develops a researcher&rsquo;s capacity in an '
    'interdisciplinary area &mdash; and through outreach that brings plant science to non-specialist '
    'audiences.'))
A(P('Economic impact.',
    'No direct commercial outcome is expected within the fellowship, as this is fundamental research. In '
    'the longer term, knowledge of how meristem activity is set by temperature could inform breeding '
    'programmes seeking varieties with architecture optimised for a warming climate or for high-density '
    'planting, and the identification of redox-regulated components could provide targets for '
    'biotechnological modulation of meristem activity. The fellowship also contributes to the European '
    'Research Area by strengthening research capacity at the host institution &mdash; installing an in '
    'vivo redox capability that remains available after the project ends &mdash; and by training a '
    'researcher whose combined skill set is scarce.'))

A('<h1>3. Quality and Efficiency of the Implementation</h1>')
A('<h2>3.1&nbsp;&nbsp;Quality and effectiveness of the work plan, assessment of risks and appropriateness '
  'of the effort assigned to work packages</h2>')
A(P('', 'The project is organised into three scientific work packages (WP1&ndash;WP3) that together answer '
     'one question &mdash; how the shoot apical meristem reads temperature to set the plastochron &mdash; '
     'plus a management and training work package (WP4) and a dissemination work package (WP5). The '
     'scientific WPs are sequenced so that each constrains the next while remaining individually '
     'informative. WP1 establishes the temperature response of the meristem on a thermal-time basis and '
     'fixes the developmental time windows and reporter lines used downstream. WP2 tests the two candidate '
     'transducers &mdash; phyB and the redox/NO system &mdash; against that baseline. WP3 profiles the '
     'response at single-cell resolution under a design that separates temperature from developmental '
     'stage. The decisive result of the project &mdash; whether NO perturbation reproduces the loss of '
     'thermal-time compensation seen in phyB &mdash; lies in WP2 and does not depend on the success of the '
     'more exploratory WP3.'))
A(P('Interdependencies and critical path.',
    'T1.1 (plastochron phenotyping) is the first experiment and the critical-path entry point: it is '
    'technically straightforward, uses an assay I have already established, and its per-genotype linear '
    'models define which temperatures, time windows and genotypes are carried into WP2 and WP3. Live '
    'imaging (T1.2) and the redox/NO experiments (WP2) run in parallel from M3&ndash;M6 onward. WP3 tissue '
    'collection begins once T1.1 has fixed the two thermal-time points (M8), with a pilot sequencing run '
    'before the full factorial. Long-lead work &mdash; crosses of the NO-pathway mutants into the pCLV3, '
    'pWUS, DR5 and PIN1 reporter backgrounds &mdash; starts in M1 to accommodate the 6&ndash;8-week '
    'Arabidopsis generation time.'))
A(P('Effort.',
    'The action supports one researcher for 24 months (24 person-months), distributed approximately as '
    'WP1 7 PM, WP2 8 PM, WP3 6 PM, WP4 1 PM and WP5 2 PM. WP2 carries the largest share because it '
    'contains the decisive experiment and the widest range of techniques (in vivo imaging, histochemistry, '
    'pharmacology, genetics, biotin-switch). WP3 is deliberately bounded: the factorial design and the '
    'collaboration with the Reis group (University of Bern) keep the single-cell component to a defined, '
    'well-supported task rather than an open-ended screen. The 24-month duration is appropriate &mdash; '
    'WP1 completes by M12, WP2 by M20, and the WP3 dataset is deposited by M24, leaving the final months '
    'for analysis, write-up and the second manuscript.'))

# ---- Table 1: Gantt (PIL PNG, embedded) ----
gpng = os.path.join(OUT_DIR, "gantt.png")
make_gantt(gpng)
g_b64 = base64.b64encode(open(gpng, "rb").read()).decode()
A('<p class="caption">Table 1. Work-package schedule (months 1&ndash;24).</p>')
A(f'<img src="data:image/png;base64,{g_b64}" width="638">')
A('<p class="legend">Bars = task active; &#9670; = milestone. WP1 blue, WP2 green, WP3 orange, '
  'WP4 grey, WP5 pink; long-lead crossing work in light grey. Task titles as in section 1.2.</p>')

# ---- Table 2: Deliverables & Milestones ----
dm = [
 ("D1","Career Development Plan","WP4","3"),
 ("D2","Data Management Plan (FAIR)","WP4","6"),
 ("D3","Report: temperature response of the SAM (WP1)","WP1","12"),
 ("D4","Curated dataset: redox/NO maps and perturbation phenotypes","WP2","20"),
 ("D5","Processed single-nucleus dataset, deposited with a persistent identifier","WP3","24"),
 ("D6","Manuscript 1 (WP1+WP2) posted as a preprint at submission","WP5","22"),
 ("D7","Manuscript 2 (WP3) posted as a preprint at submission","WP5","24"),
 ("M1","Temperatures, time windows and reporter/mutant set fixed for WP2&ndash;WP3","WP1","6"),
 ("M2","Decisive experiment concluded: does NO perturbation phenocopy phyB?","WP2","18"),
 ("M3","Temperature- and thermal-time-responsive gene networks of the SAM defined","WP3","22"),
]
A('<p class="caption">Table 2. Deliverables (D) and milestones (M).</p>')
A('<table class="tbl"><tr><th>ID</th><th>Title</th><th>WP</th><th>Month</th></tr>' +
  "".join(f'<tr><td class="c">{i}</td><td>{t}</td><td class="c">{w}</td><td class="c">{mo}</td></tr>'
          for i,t,w,mo in dm) + '</table>')

# ---- Table 3: Risks ----
risks = [
 ("The phyB thermal-time phenotype does not hold under controlled temperature shifts, or effect sizes "
  "are small.","L","M",
  "The phenotyping assay is already established and gives robust per-genotype linear models; multiple "
  "constant temperatures and shift regimes; increased replication; independent readouts (leaf number, "
  "SAM size, reporter domains)."),
 ("NO perturbation produces no plastochron phenotype.","M","M",
  "A null result still discriminates between models and is publishable: Task 2.1 independently tests the "
  "ROS branch, and pharmacology, genetics and reporter localisation triangulate. The glutathione control "
  "separates NO-specific from general thiol-redox effects."),
 ("Single-nucleus RNA-seq under-samples the meristem, or nuclei yield from the vegetative apex is low.",
  "M","M",
  "Micro-dissection enrichment of the apex; pilot run at M8 before the full factorial; the Reis group has "
  "aerial-tissue protocols; fallback to reporter-sorted low-input RNA-seq of zonal populations."),
 ("Delay or reduced availability in the Reis collaboration.","L","M",
  "Written work plan and scheduled technical visits from M1; sequencing can be outsourced to a core "
  "facility; analysis pipelines are portable and partly covered by SIB courses."),
 ("CherryTemp live-imaging of the apex is technically demanding (drift, phototoxicity, z-range).","M","L",
  "The system and confocal are installed and in routine use in the host lab; start with stable set-points "
  "before rapid shifts; WP1's core result (T1.1) does not depend on live imaging."),
 ("Arabidopsis line generation slower than the 6&ndash;8-week cycle allows.","M","L",
  "Reporter and mutant lines are already in the host lab; crosses started in M1; staggered sowing."),
 ("24 months too short for two manuscripts.","L","M",
  "Manuscript 1 (WP1+WP2) is self-contained and targeted for M22; the WP3 dataset is a standalone "
  "deliverable (M24) whose paper may be completed shortly after tenure."),
]
A('<p class="caption">Table 3. Risk assessment (L = low, M = medium, H = high).</p>')
A('<table class="tbl">'
  '<colgroup><col style="width:32%"><col style="width:5%"><col style="width:5%"><col style="width:58%"></colgroup>'
  '<tr><th>Risk</th><th>L</th><th>I</th><th>Mitigation</th></tr>' +
  "".join(f'<tr><td>{r}</td><td class="c">{l}</td><td class="c">{im}</td><td>{mit}</td></tr>'
          for r,l,im,mit in risks) + '</table>')

A('<h2>3.2&nbsp;&nbsp;Quality and capacity of the host institution and participating organisations, '
  'including hosting arrangements</h2>')
A(P('Host institution.',
    'The fellowship is hosted by the group of Prof. Martina Legris at the Institute of Biology, Faculty of '
    'Sciences, University of Neuch&acirc;tel (UniNE). The institute is an established centre for plant '
    'biology in Switzerland, with several groups working on plant development, physiology and '
    'plant&ndash;environment interactions, a shared seminar programme, and membership of the CUSO doctoral '
    'programme in plant sciences and the Swiss Plant Science Web. This gives the fellow an immediate '
    'community in plant developmental and environmental biology and structured doctoral- and '
    'postdoctoral-level training.'))
A(P('Research environment and equipment.',
    'The host group is funded by an SNSF Starting Grant (&ldquo;Environmental control of shoot '
    'architecture in Arabidopsis&rdquo;, 2023&ndash;2028) and a two-year Fondation Mercier pour la Science '
    'grant that establishes the temperature-and-leaf-initiation line this fellowship contributes to. The '
    'infrastructure the project needs is in place: a spectral confocal microscope co-funded by the '
    'supervisor (SNSF R&rsquo;equip, 2024); a CherryTemp sample-level temperature-control system for live '
    'imaging; controlled-environment growth chambers with temperature logging; and full molecular-biology, '
    'histochemistry and plant-transformation facilities. The reporter lines (pCLV3, pWUS, DR5, PIN1) and '
    'the thermosensor and NO-pathway mutants required by the project are already available in the group.'))
A(P('Supervision.',
    'Prof. Legris is a foundational contributor to plant thermomorphogenesis &mdash; first author of the '
    'work establishing phyB as a thermosensor<sup>4</sup> and of subsequent work on light and temperature '
    'control of leaf and meristem morphogenesis<sup>5&ndash;6</sup> &mdash; and holds the 2023 <i>New '
    'Phytologist</i> Tansley Medal. As a former MSCA, EMBO and HFSP fellow she knows the instrument from '
    'the inside. The group comprises the supervisor, one postdoctoral researcher and one PhD student; '
    'supervision is organised around weekly one-to-one and group meetings, a Career Development Plan '
    'reviewed at regular intervals, and quarterly progress presentations, with co-supervision of a '
    'master&rsquo;s student planned for the fellow in year 2 (see 1.3).'))
A(P('Career and open-science support.',
    'The UniNE Graduate Campus (swissuniversities 2025&ndash;2028 programme) provides transferable-skills '
    'and career training; the university&rsquo;s research and technology-transfer services support grant '
    'preparation and any exploitation questions; and the Libra institutional repository ensures Horizon '
    'Europe-compliant open access. The fellow will also access CUSO and UniNE doctoral-programme courses '
    'and the R&eacute;seau romand de mentorat pour femmes and REGARD programmes.'))
A(P('Participating organisation &mdash; University of Bern (collaboration).',
    'The single-nucleus transcriptomics of WP3 is carried out with the group of Dr R. Reis at the '
    'University of Bern (~40 minutes from Neuch&acirc;tel), which provides single-cell/nucleus methodology '
    'and computational analysis. This is a scientific collaboration involving short technical visits, not '
    'a beneficiary or associated-partner role, and no secondment is foreseen.'))

A('<h2 style="font-style:normal;font-weight:bold">References</h2>')
refs = [
 "Wenzl and Lohmann (2023), Cells &amp; Development. 175:203850",
 "Zeng et al. (2017), EMBO Journal. 36:2844&ndash;2855",
 "Zeng et al. (2023), Nature Communications. 14:8001",
 "Legris et al. (2016), Science. 354:897&ndash;900",
 "Legris et al. (2019), Nature Communications. 10:5219",
 "Legris (2023), New Phytologist. 240:2191&ndash;2196",
 "Iglesias et al. (2024), PNAS. 121:e2320187121",
 "Luquet et al. (2025), Plant Science. 352:112377",
 "Nejamkin et al. (2025), Journal of Plant Growth Regulation. 44:5147&ndash;5159",
]
A('<div class="refs">' + "".join(f'<p>{i+1}&nbsp;&nbsp;{r}</p>' for i,r in enumerate(refs)) + '</div>')
A('<p class="rule">--------------------------------------- End of page count (max 10 pages) '
  '---------------------------------------</p>')

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(blocks)}</body></html>"
htmlpath = os.path.join(OUT_DIR, "merged_b1.html")
open(htmlpath, "w", encoding="utf-8").write(html)

subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", OUT_DIR, htmlpath],
               check=True, capture_output=True)
b1pdf = os.path.join(OUT_DIR, "merged_b1.pdf")
print("B1 pages:", pymupdf.open(b1pdf).page_count)

# assemble: new B1 + original pages 9-11 (Part B-2)
out = pymupdf.open(b1pdf)
orig = pymupdf.open(ORIG)
out.insert_pdf(orig, from_page=8, to_page=10)
out.save(FINAL)
print("FINAL:", FINAL, "pages:", out.page_count)
