# Luquet — MSCA PF Part B-1 — revised RED text

Workflow: plain text below, section by section. Paste into your Word template and
normalise to the body font (Times New Roman 11). British/EU spelling throughout.
Citations: the whole of Part B-1 is unified to superscript numerals with one
reference list in the MSCA_B1 ZOE compact format — see the "CITATION UNIFICATION"
block near the end for the master list and every in-text position (black + red).

================================================================================
§1.1  EXCELLENCE — objectives
================================================================================

--- REPLACE the WP2 stub -------------------------------------------------------

WP2: Role of phyB and of redox/NO signalling in the temperature control of leaf
initiation. I will test whether the canonical thermosensor phyB and the meristem
redox/NO system transduce temperature into plastochron regulation. Task 2.1
addresses the general redox state of the meristem — the superoxide/H2O2 balance
across the central and peripheral zones — as a function of temperature; Task 2.2
addresses nitric oxide specifically, through in vivo detection, NO donors and
scavengers, and NO-pathway mutants, asking whether NO perturbation reproduces the
phyB phenotype established in my preliminary work.

--- REPLACE the WP3 stub -------------------------------------------------------

WP3: Single-cell transcriptomic response of the SAM to warm temperature. Using a
factorial temperature x thermal-time design, I will characterise the meristem's
temperature response at cellular resolution and test whether known meristem
regulators — the WUS/CLV3 network, zonal redox and NO-biosynthesis genes, and
auxin readouts — participate in temperature and thermal-time sensing. This yields
the temperature- and redox-responsive gene networks of the SAM and a reusable
community dataset, and is carried out with R. Reis (University of Bern).

--- REPLACE "Originality and ambition." --------------------------------------

Originality and ambition. Three features make the project original. First, it
moves temperature signalling out of the hypocotyl, where it is almost exclusively
studied, and into the shoot apical meristem, where the organs that shape the plant
are initiated. Second, it proposes a specific, testable transducer — a redox/NO
node in the peripheral zone — rather than treating meristem thermosensing as a
generic unknown: my preliminary data establish that phyB is required to hold the
plastochron on a constant thermal-time relationship, a meristem phenotype distinct
from the canonical hypocotyl-elongation output, and I propose that phyB acts here
through a redox/NO route rather than the PIF4/COP1 growth-effector branch. Third,
it connects two fields that have developed in parallel — thermomorphogenesis,
which has identified the sensors, and the redox biology of the stem-cell niche,
which provides the positional signals that pattern organ initiation. Establishing
how an environmental cue is converted into the timing of organ formation is of
broad significance for developmental biology and directly relevant to crop
resilience under a warming climate, where the rate of leaf initiation shapes
canopy establishment and yield.

--- WP1 TITLE (black-text exception, approved) -------------------------------

Change  "WP1: Characterization of temperature on early development in the meristem."
to      "WP1: Characterisation of the temperature response of the meristem during
         early development."

--- STATE OF THE ART, end of the redox paragraph (black-text edit, approved) --

DELETE the trailing sentence fragment:
  "The meristem redox state is further shaped by its microenvironment: the
   stem-cell niche is hypoxic, and low oxygen is itself a developmental signal
   transduced"
End that paragraph at "... (Zeng et al., 2023)." [-> superscript once converted]

--- NEW paragraph under the (currently empty) "Preliminary results." heading ---

Preliminary results. Using a thermal-time phenotyping assay restricted to the
vegetative phase, I have compared wild type and the thermosensor mutant phyB
across temperatures. Wild type holds the plastochron on an essentially constant
thermal-time relationship, whereas phyB does not: its leaf-initiation rate departs
from the thermal-time expectation (Fig. 1). This identifies a meristem-level
temperature phenotype for phyB, distinct from its established role in hypocotyl
elongation, and it is the observation on which the project is built. I have also
begun to manipulate NO in the apex with the donor GSNO and the scavenger cPTIO,
read on the same thermal-time basis; these experiments are in progress and have
not yet produced a clear plastochron phenotype, and establishing whether NO acts
downstream of temperature in the meristem is the central question of WP2. The
reporter lines (pCLV3, pWUS, DR5, PIN1) and the CherryTemp-based live-imaging
required for WP1 are in place in the host laboratory.
[Figure 1 to be supplied by applicant.]

================================================================================
§1.2  METHODOLOGY
================================================================================

REPLACE everything from "By objective." through the end of "Open science."
(this also absorbs the old "scRNA-seq design." block) with the following.
The "Sex and gender dimension." paragraph that follows stays as-is (black).

--------------------------------------------------------------------------------

Overall approach. The methodology pairs two logics rarely combined in one
laboratory: the quantitative, imaging-based developmental biology of the shoot
apical meristem, and the biochemistry of nitric oxide and redox signalling. A
single output — the rate and pattern of organ initiation, expressed on a
thermal-time basis — is read through three complementary lenses (genetic and
phenotypic, in vivo imaging, and biochemical), so that no central claim rests on
one technique. All experiments are restricted to the vegetative phase and
controlled for flowering time, and thermal time is computed from logged
growth-chamber temperatures, so that chronological age and developmental
progression are separated throughout.

WP1 — Characterisation of the temperature response of the meristem during early
development.

Task 1.1 — Plastochron and phyllotaxis against thermal time. I will quantify the
plastochron and the phyllotactic divergence angle in wild type and selected
mutants (phyB and the NO-pathway mutants used in WP2), grown at contrasting
constant temperatures and under defined temperature shifts. Per-genotype linear
models of leaf number against thermal time are compared statistically to
establish whether each genotype maintains a constant thermal-time relationship
(compensation) or departs from it.

Task 1.2 — Live imaging of meristem and auxin reporters under controlled
temperature. Using the stem-cell reporters pCLV3 and pWUS and the auxin reporters
DR5 and PIN1, I will image the living apex by confocal microscopy on the spectral
confocal microscope recently acquired by the Institute of Biology (SNSF R'equip,
2024), with temperature controlled at the sample by the CherryTemp system
available in the host laboratory (stable set-points and rapid shifts during
time-lapse). Readouts — SAM size, the size and position of the WUS and CLV3
domains, the position of PIN1-dependent auxin maxima, and the timing of primordium
emergence — are each placed on a thermal-time axis.

WP2 — Role of phyB and of redox/NO signalling in the temperature control of leaf
initiation.

Task 2.1 — Temperature and the redox compartmentalisation of the meristem. I will
map reactive redox species in the living apex across temperatures and in phyB: the
superoxide/hydrogen peroxide balance (DHE and NBT for O2.-; H2DCFDA and DAB for
H2O2), quantified by confocal imaging and histochemistry. The question is whether
warm temperature reconfigures the central-versus-peripheral redox pattern
described by Zeng et al.^{2,3}, and whether any such change depends
on phyB.

Task 2.2 — Nitric oxide as a candidate temperature transducer. NO is detected in
vivo with DAF-FM DA and perturbed genetically (gsnor1/hot5, nia1 nia2, noa1) and
pharmacologically (the donor GSNO and the scavenger cPTIO; glutathione as a
control for the general thiol-redox context, not as an NO-specific treatment).
All perturbations are read on a thermal-time basis and compared directly with the
phyB phenotype. My preliminary data establish that phyB fails to hold the
plastochron on a constant thermal-time relationship; NO manipulations are in
progress and have not yet produced a clear phenotype. The decisive experiment of
this task is whether NO perturbation reproduces this loss of thermal-time
compensation. NO-pathway mutants are crossed with the DR5, PIN1, WUS and CLV3
reporters to localise any effect within the meristem, and candidate
S-nitrosylation targets in the stem-cell niche (e.g. AGO4) are probed by
biotin-switch assays.

WP3 — Single-cell transcriptomic response of the SAM to warm temperature.

Comparing two temperatures at equal chronological age confounds temperature with
developmental stage (warm develops faster); comparing at equal thermal time
controls development but not chronological age.

Task 3.1 — Factorial temperature x thermal-time design. I will profile dissected
vegetative apices by single-nucleus RNA-seq under a factorial design: two
temperatures (control vs warm) x two matched thermal-time points, rather than a
gradient, which for single-cell work would dilute replication and power. This
separates the effect of temperature at matched development from the effect of
developmental progression and provides a direct test of compensation: a gene
genuinely compensated on a thermal-time basis should not differ between
temperatures once thermal time is matched.

Task 3.2 — Analysis and candidate networks. Predictions from Zeng et
al.^{2,3} anchor quality control and a targeted analysis panel:
WUS/CLV3 targets, AGO4 and RdDM components, zonal ROS-metabolising enzymes, the
NO-biosynthesis genes NIA1, NIA2 and NOA1, and auxin readouts. Library
preparation and single-cell analysis are carried out in collaboration with
R. Reis (University of Bern), who provides the single-cell transcriptomics
expertise; short technical visits to Bern are foreseen for the wet-lab and
computational steps.

Interdisciplinarity. The project sits at the interface of developmental biology,
plant physiology and redox biochemistry. Its feasibility rests on combining
expertise that does not currently coexist in one place: the host's developmental
and photobiological framework and quantitative live-imaging, my own redox/NO
biochemistry and in vivo detection, and the single-cell transcriptomics of the
Reis group.

Open science. Data are managed under a FAIR-compliant Data Management Plan
prepared in the first months and updated thereafter. Datasets underlying
publications — imaging, quantitative phenotyping and the single-nucleus dataset —
are deposited in recognised community repositories with persistent identifiers.
Publications are made immediately open access and deposited in Libra, the
institutional repository of the University of Neuchâtel, with preprints posted at
submission. Protocols and analysis code, including the thermal-time image-analysis
and statistical pipelines, are shared openly, and confirmatory analyses are
pre-registered where possible.

================================================================================
§1.3  SUPERVISION, TRAINING, TWO-WAY TRANSFER
================================================================================

--- "What I gain from the host." — REPLACE the red tail (from "My training plan
    centres...") -------------------------------------------------------------

My training plan centres on three scientific competences the project requires and
that I do not yet have: quantitative live-imaging of the meristem (reporter lines,
temperature-controlled imaging with CherryTemp, 3D image-analysis pipelines); the
genetics and conceptual framework of thermomorphogenesis, a field to which my
supervisor is a foundational contributor; and single-nucleus transcriptomics
together with its computational analysis. Technical training is provided within
the host group and, for the single-cell work, through the collaboration with
R. Reis (Bern) and dedicated courses of the Swiss Institute of Bioinformatics
(bulk and single-cell RNA-seq analysis). Transferable-skills and career training
is provided by the UniNE Graduate Campus (part of the swissuniversities 2025–2028
programme for the promotion of academic talent) and by the doctoral programmes of
UniNE and the CUSO; I will also attend the EMBO Laboratory Leadership for Postdocs
course and present at international plant photobiology and thermomorphogenesis
meetings, including those co-organised by my supervisor in 2026.

--- "What I bring to the host." — REPLACE (light rewrite) --------------------

What I bring to the host. The host group has no in vivo redox capability. I bring
the detection of reactive redox species in living tissue (DAF-FM DA for NO;
H2DCFDA and DHE for ROS), the genetics of NO homeostasis, the pharmacological
manipulation of NO with donors and scavengers, and the biochemistry of
cysteine-based post-translational modifications, including biotin-switch
workflows. The group's interest in redox as an integrator of environmental and
endogenous cues in the meristem is explicit and current — for example in the
shade-induced ROS/NO work my supervisor co-authored^7 — but the technical
capacity to pursue it in vivo is not yet established in
Neuchâtel. My arrival makes that line executable and installs a capability that
will outlive the fellowship: a genuine two-way transfer of knowledge.

--- "Quality of supervision." — REPLACE red spans + FILL the [Completar:] block
    (two paragraphs) --------------------------------------------------------

Quality of supervision. Prof. Martina Legris leads a research group at the
Institute of Biology, University of Neuchâtel. She specialises in the molecular
signalling of photoreceptors and in developmental plasticity in response to light
and temperature, with over 20 publications including first- or corresponding-
author papers in Science, PNAS, Nature Communications, New Phytologist and Plant
Physiology, and she received the 2023 New Phytologist Tansley Medal. Her
contribution is foundational: she is first author of the work establishing phyB as
a thermosensor that integrates light and temperature in Arabidopsis^4, and she has
since developed the study of light and temperature control of leaf and meristem
morphogenesis^{5,6,7}. She
trained in the Casal and Fankhauser laboratories and is herself a former MSCA,
EMBO and HFSP fellow, so she knows the fellowship from the inside. My project is a
direct extension of a question her own work opened — how temperature is read in
the meristem to set leaf initiation — which makes the supervision scientifically
substantive.

The group comprises the supervisor, one postdoctoral researcher and one PhD
student, with a second postdoc (myself) joining on this project; the supervisor
has additionally mentored numerous master's and summer students. It is funded by
an SNSF Starting Grant (TMSGI3_218178, "Environmental control of shoot
architecture in Arabidopsis", 2023–2028) and by a two-year Fondation Mercier pour
la Science grant ("Temperature regulation of leaf initiation in Arabidopsis
thaliana", 2026) that establishes the research line this fellowship contributes
to, with access to a spectral confocal microscope co-funded by the supervisor
(SNSF R'equip, 2024). Supervision is organised around weekly one-to-one and group
meetings, a Career Development Plan agreed in the first months and reviewed at
regular intervals, and quarterly progress presentations. In the second year I
will co-supervise, with the supervisor's support, a master's student on a defined
part of the project.

--- "Secondment." — FILL the empty heading -----------------------------------

Secondment. No secondment is foreseen. The single-nucleus transcriptomics of WP3
is carried out through a scientific collaboration with the group of Dr R. Reis
(University of Bern), involving short technical visits rather than a formal
secondment.

================================================================================
§1.4  RESEARCHER'S EXPERIENCE, COMPETENCES AND SKILLS
================================================================================

In the sentence about the Paris-Saclay research stay:

- REPLACE the red phrase "AGO4/DNA-methylation dimension of this project" with:
  "AGO4/RdDM dimension of the redox–meristem link addressed in WP2 and WP3"
  (full clause: "...whose expertise in chromatin biology and DNA methylation
  connects directly to the AGO4/RdDM dimension of the redox–meristem link
  addressed in WP2 and WP3.")

- REPLACE the placeholder "(CITA)" with superscript ^9 (Nejamkin et al. 2025;
  ref 9 in the list below). Full clause after the tidy:
  "...collaborations of my own, including with Lamattina's group in Mar del Plata
  (2021), which resulted in a co-authored paper^9, and a research stay in the
  Chromosome Dynamics group at IPS2, Université Paris-Saclay (2025), whose
  expertise in chromatin biology and DNA methylation connects directly to the
  AGO4/RdDM dimension of the redox–meristem link addressed in WP2 and WP3."

- In the earlier sentence, "published as first author (Luquet et al., Plant
  Science, 2025)" -> "published as first author^8".

================================================================================
§2.1  IMPACT — career perspectives
================================================================================

REPLACE the whole subsection (heading is red too).

2.1 Credibility of the measures to enhance the career perspectives and
employability of the researcher and contribution to their skills development

My long-term objective is to lead an independent research group at the interface
of redox biology and plant development. This fellowship is the decisive step
towards that goal: it adds to my established expertise in nitric oxide and redox
physiology the three competences this research programme requires and that I
currently lack — quantitative live-imaging of development at cellular resolution,
the genetics and conceptual framework of thermomorphogenesis, and single-cell
transcriptomics with its computational analysis. Acquiring these in a group
working at the interface of light, temperature and shoot development positions me
to lead a distinctive line of research that few others can, precisely because it
joins two communities that rarely meet.

My skills development is organised around a Career Development Plan, agreed with my
supervisor in the first months of the fellowship and reviewed at regular
intervals, which sets objectives for research training, transferable skills and
career progression. Scientific training follows the work packages: WP1 and WP2
build my competence in reporter-based confocal imaging, temperature-controlled
live-imaging and image quantification, while WP3, with the Reis group in Bern,
introduces me to single-nucleus transcriptomics and the bioinformatic analysis of
complex datasets, an increasingly indispensable skill in plant developmental
biology.

Transferable skills are supported by the host institution. The UniNE Graduate
Campus, established under the swissuniversities 2025–2028 programme for the
promotion of academic talent, offers workshops and courses for the career
development of postdoctoral researchers, and I will also have access, subject to
availability, to courses of the doctoral programmes of UniNE and the CUSO. I will
use this provision to strengthen the competences an independent researcher needs
beyond the bench: scientific writing and grant preparation, project and data
management, research integrity, and leadership and supervision — the last
supported by the EMBO Laboratory Leadership for Postdocs course. I will further
participate in the Réseau romand de mentorat pour femmes and the REGARD workshop
programme, which support the progression of women towards independent academic
positions.

Supervision experience is a deliberate part of the plan: in the second year I
will propose and co-supervise a master's student on a defined part of the
project, with my supervisor's support, gaining first-hand experience of mentoring
and of scoping a project for a student. Together with the teaching experience I
bring from Argentina, this prepares me for the training responsibilities of a
group leader.

Finally, the fellowship substantially widens my network. Beyond the host group,
Switzerland's position and my supervisor's collaborations give me access to the
European plant-science community, and I will present my results at international
conferences — the International Conference on Arabidopsis Research (ICAR), the
EPSO Plant Biology Europe congress, and thermomorphogenesis and plant-development
meetings — and at institutional seminars. Combined with my international
trajectory across Argentina, France and Switzerland, and a portfolio that will by
then span redox biochemistry, developmental imaging and single-cell genomics,
this makes me competitive for independent-investigator schemes such as the SNSF
Ambizione and Starting Grants and the ERC Starting Grant, whether I continue in
Europe or return to Latin America, where these competences are scarce.

================================================================================
§2.2  IMPACT — dissemination, exploitation, communication
================================================================================

REPLACE the whole subsection.

2.2 Suitability and quality of the measures to maximise expected outcomes and
impacts, as set out in the dissemination and exploitation plan, including
communication activities

Dissemination. The primary route for disseminating results is peer-reviewed
publication. I anticipate at least two papers: a first on the characterisation of
the temperature response of the SAM (WP1) together with the redox and NO
perturbation experiments (WP2), and a second built on the single-nucleus dataset
(WP3). Because the project sits at the intersection of two communities, I will
target journals read by both plant developmental biologists and the
environmental-signalling and redox fields, and I will post preprints at the time
of submission so that results reach both communities without delay. I will publish
open access and deposit the accepted versions in Libra, the institutional
open-access repository of the University of Neuchâtel, in compliance with Horizon
Europe requirements.

Results will also be disseminated at the international conferences listed in
section 2.1 and at specialised meristem-biology meetings, through seminars at
UniNE and partner institutions, and through the collaboration with the Reis group.
Presenting to audiences of different composition, from a specialised
meristem-biology audience to a broader plant-science one, is itself part of my
training in scientific communication.

Research data are a deliverable in their own right. All data underlying
publications — imaging data, quantitative phenotyping datasets and the
single-nucleus transcriptomic dataset — will be managed under a Data Management
Plan following the FAIR principles and deposited in recognised community
repositories with persistent identifiers. The single-nucleus dataset of the SAM
temperature response (WP3) is designed as a reusable community resource: there are
few single-cell datasets of the vegetative shoot apex and none, to my knowledge,
addressing temperature, so its value extends well beyond the questions I ask of it
here. Protocols and analysis code, including the thermal-time quantification and
image-analysis pipelines, will be shared openly so that the methods are reusable.

Exploitation. The project is basic research and no intellectual property is
anticipated at the outset. However, leaf-initiation rate is a determinant of
canopy establishment and yield, and identifying redox-based mechanisms that set it
could open routes to modulate meristem activity, whether through breeding targets
or through chemical modulation of redox signalling. Should an exploitable result
emerge, I will assess it with my supervisor and with the research and
technology-transfer services of the University of Neuchâtel, and any decision on
protection will be taken before publication.

Communication. Communication activities are distinct from dissemination and are
directed at audiences beyond the scientific community. I have a sustained record
of public engagement — Fascination of Plants Day, university science festivals and
open-science advocacy in Argentina — and I will continue this in Neuchâtel through
the university's public-engagement programme [specify local formats, e.g. Jardin
botanique de Neuchâtel, Fascination of Plants Day, Pint of Science]. The message I
will build for general audiences connects the project to something tangible: how
plants decide when to make a leaf, and why that decision matters as temperatures
rise. I will also contribute to institutional communication channels and press
releases where results warrant it, and use social media to reach the wider
plant-science and student community. As a woman researcher trained in Latin
America and working in Europe, I see value in making that trajectory visible to
students considering research careers, and I will seek opportunities to do so.

================================================================================
§2.3  IMPACT — magnitude and importance
================================================================================

REPLACE the whole subsection.

2.3 The magnitude and importance of the project's contribution to the expected
scientific, societal and economic impacts

Scientific impact. The project addresses a gap that is conspicuous once stated:
temperature is one of the strongest environmental regulators of plant form, and
the shoot apical meristem is where plant form originates, yet the mechanisms
linking the two are essentially unknown. Almost everything known about plant
thermosensing comes from the hypocotyl, a tissue whose response is driven by cell
expansion. By asking the same question in the meristem, where the relevant
processes are stem-cell homeostasis, cell division and differentiation, the
project tests whether the established thermosensory framework generalises or
whether the meristem uses a different logic; my preliminary data point to the
latter, which would be a substantive contribution in itself. Beyond this, the
project brings redox and nitric oxide signalling into contact with
thermomorphogenesis, two fields that have developed largely in parallel, and
delivers a single-nucleus dataset of the temperature response of the shoot apex
that will serve as a community resource. Because few groups work on the
environmental regulation of meristem activity, and because I will work at the
interface of the developmental and temperature-signalling communities, I expect
the results to be of broad interest across plant biology.

Societal impact. The rate at which leaves are produced determines how quickly a
canopy is established, and canopy establishment governs light capture, water use
and ultimately yield. This relationship is conserved from Arabidopsis to crops
such as rice and maize. Under climate change, with rising mean temperatures and
more frequent warm episodes, the temperature dependence of leaf initiation
becomes directly relevant to how crops perform in the field. Understanding the
mechanism that sets this rate is a prerequisite for any strategy that seeks to
adjust it, and contributes to the broader European objectives of climate-resilient
and sustainable agriculture and of food security. The project also contributes to
society through training — it develops a researcher's capacity in an
interdisciplinary area — and through outreach that brings plant science to
non-specialist audiences.

Economic impact. No direct commercial outcome is expected within the fellowship,
as this is fundamental research. In the longer term, knowledge of how meristem
activity is set by temperature could inform breeding programmes seeking varieties
with architecture optimised for a warming climate or for high-density planting,
and the identification of redox-regulated components could provide targets for
biotechnological modulation of meristem activity. The fellowship also contributes
to the European Research Area by strengthening research capacity at the host
institution — installing an in vivo redox capability that remains available after
the project ends — and by training a researcher whose combined skill set is
scarce.

================================================================================
CITATION UNIFICATION — whole of Part B-1 (§1.1–§1.4)
================================================================================

STYLE: every in-text citation becomes a superscript numeral (no author-year in
the running text), numbered in order of first appearance. One reference list in
the MSCA_B1 ZOE compact format:  "N  Author et al. (year), Journal. vol:pages".
Place it as page-bottom footnotes or a short end block, matching the template.

--------------------------------------------------------------------------------
MASTER REFERENCE LIST (final numbering)
--------------------------------------------------------------------------------
1  Wenzl and Lohmann (2023), Cells & Development. 175:203850
2  Zeng et al. (2017), EMBO Journal. 36:2844–2855
3  Zeng et al. (2023), Nature Communications. 14:8001
4  Legris et al. (2016), Science. 354:897–900
5  Legris et al. (2019), Nature Communications. 10:5219
6  Legris (2023), New Phytologist. 240:2191–2196
7  Iglesias et al. (2024), PNAS. 121:e2320187121
8  Luquet et al. (2025), Plant Science. 352:112377
9  Nejamkin et al. (2025), Journal of Plant Growth Regulation. [add vol:pages]

--------------------------------------------------------------------------------
IN-TEXT SUPERSCRIPTS — every position in the document
--------------------------------------------------------------------------------
BLACK text — find / replace (only the citation marker changes):

  §1.1 Introduction
    "...linearly related to the thermal time1: the amount of degrees the plant
     experience over a period of time."
    ->  "...linearly related to thermal time — the number of degree-days the
         plant experiences over a given period."
    (removes the stray superscript "1", which had no reference; fixes grammar.
     If you want a citation for the thermal-time concept, add e.g. Parent and
     Tardieu (2012), New Phytologist. 194:760-774 and renumber.)

  §1.1 State of the art
    "...WUS/CLV3 expression patterns (Wenzl and Lohmann, 2023)."
        -> "...WUS/CLV3 expression patterns^1."
    "...reduces SAM size and delays early leaf development (Zeng et al., 2017;
     Zeng et al., 2023)."
        -> "...reduces SAM size and delays early leaf development^{2,3}."
    "...WUS interacting with AGO4 in a NO-dependent manner (Zeng et al., 2023)."
        -> "...WUS interacting with AGO4 in a NO-dependent manner^3."

  §1.1 Hypocotyl-thermosensing paragraph — add two citations already in the list
     (no renumbering). Also "signaling" -> "signalling".
       "...phytochrome B (phyB) acts as a thermosensor inactivated at warm
        temperature;"
          -> "...inactivated at warm temperature^4;"
       "...Downstream, signaling converges on PIF4 and the E3 ligase COP1."
          -> "...Downstream, signalling converges on PIF4 and the E3 ligase
             COP1^5."
     (ref 4 = Legris et al. 2016, primary phyB paper; ref 5 = Legris et al. 2019
     Nat Commun review — the only thermosensing references in Scientific_
     proposal.pdf; it covers phyB/PIF4/PIF7/COP1. No dedicated ELF3 or PIF7
     primary paper is available in that bibliography.)

  §1.4
    "published as first author (Luquet et al., Plant Science, 2025)"
        -> "published as first author^8"

RED text — already marked in the drafts above:
  §1.2 Task 2.1   "...described by Zeng et al.^{2,3}"
  §1.2 Task 3.2   "Predictions from Zeng et al.^{2,3}"
  §1.3 Quality of supervision   phyB thermosensor -> ^4 ;
       "leaf and meristem morphogenesis" -> ^{5,6,7}
  §1.3 What I bring   "...work my supervisor co-authored^7"
  §1.4   "...a co-authored paper^9..."

NOTE: "^N" and "^{N,M}" denote superscripts — format them as superscript on
paste; do not leave the caret/braces in the text.

================================================================================
CHANGE LOG
================================================================================

§1.1  WP2/WP3 stubs -> full parallel objective statements with Task sub-labels.
      Originality paragraph rewritten (3-point structure; phyB logic corrected so
      the PIF4/COP1 claim is a hypothesis, not a data claim).
      WP1 title grammar fixed (black).
      Dangling hypoxia sentence deleted (black).
      New "Preliminary results." paragraph added under the empty heading (black
      heading), with a (Fig. 1) call-out for the applicant-supplied figure.
§1.2  "By objective." + "scRNA-seq design." collapsed into a Task-structured
      methodology (Overall approach / WP1 T1.1-1.2 / WP2 T2.1-2.2 / WP3 T3.1-3.2 /
      Interdisciplinarity / Open science).
      Hypoxic-niche / N-degron / ERF-VII strand CUT.
      "Mohanty et al. 2026" phyB-RBOHD-FERONIA sentence CUT.
      "CherryTemp system available in the host laboratory" kept (confirmed).
      Confocal named (SNSF R'equip 2024, confirmed).
      "single-cell" -> "single-nucleus RNA-seq" (confirmed).
      biotin-switch / AGO4 sentence kept in Task 2.2 (confirmed).
      Reis (Bern) collaboration + short technical visits (confirmed).
§1.3  Training tail rewritten; SIB courses + EMBO Lab Leadership named.
      "What I bring" lightly rewritten; Iglesias 2024 citation added.
      Supervisor paragraph: [>20] -> "over 20 ..."; Tansley Medal added; MSCA/
      EMBO/HFSP; Institute de Biologie -> Institute of Biology.
      [Completar:] block filled: group = supervisor + 1 postdoc + 1 PhD + Melisa;
      funding = SNSF Starting Grant TMSGI3_218178 + Fondation Mercier 2026 +
      SNSF R'equip 2024; weekly 1:1 + group meetings + CDP + quarterly reviews;
      year-2 master's-student co-supervision.
      "Secondment." heading filled: none foreseen; Reis = collaboration not
      secondment.
§1.4  red phrase reworded; (CITA) -> Nejamkin et al. 2025 (published, ref 9);
      Luquet et al. 2025 -> ref 8; double "collaborations" tidied.
CITES Whole of B-1 unified to superscript numerals + one ZOE-format list (see
      "CITATION UNIFICATION" block). 9 references. Ref 1 = Wenzl and Lohmann
      (2023), Cells & Development. 175:203850. Hypocotyl-thermosensing paragraph
      cited with refs 4 and 5. Ref 9 vol:pages still to add.
§2.1  [Weits/Utrecht secondment] sentence removed; WP3/Bern training folded in.
      conference placeholder filled (ICAR / EPSO Plant Biology Europe /
      thermomorphogenesis & development). "his/her" -> "their". EMBO Lab
      Leadership + year-2 master's student aligned with §1.3.
§2.2  conference [specify] -> "listed in section 2.1".
      tech-transfer office [confirmar] -> generic "research and
      technology-transfer services of the University of Neuchâtel".
      public-engagement [specify] -> bracketed examples kept for you to confirm.
      "single-cell" -> "single-nucleus".
§2.3  kept almost verbatim; British spelling; "single-nucleus"; "objective" ->
      "objectives".
Global (red only): British/EU spelling; author-year -> superscript in the
      sections above.

================================================================================
REMAINING TODOs  (need you / out of today's red-only scope)
================================================================================

1. Figure 1 — applicant to supply (phyB thermal-time / plastochron phenotype).
   Referenced from the new "Preliminary results." paragraph.
2. DONE — whole document unified to superscript numerals + one ZOE-format
   reference list (see "CITATION UNIFICATION" block). Ref 1 (Wenzl & Lohmann
   2023) now complete. Outstanding: ref 9 (Nejamkin et al. 2025) add vol:pages
   now it is published.
3. DONE — hypocotyl-thermosensing paragraph cited with refs 4 and 5 (the
   thermosensing references available in Scientific_proposal.pdf). Note: no
   ELF3- or PIF7-specific primary paper exists in that bibliography, so the
   Legris et al. 2019 review (ref 5) umbrella-covers them; add primary papers
   later if a reviewer expects them.
4. Section numbering: the doc uses "1." "2." "3." then "1.4" under "1. Excellence".
   MSCA template is 1.1 / 1.2 / 1.3 / 1.4. Cosmetic; recommend fixing.
5. Project has a short title only inside the text ("...linking temperature
   perception to plastochron regulation"). MSCA B1 usually carries a project
   title + acronym at the top (cf. "Light2Shape" in the ZOE sample). Add?
6. §3 (Quality and Efficiency of the Implementation) is still "Insert here text
   for your proposal" — Gantt chart, risk table, host-capacity text all to be
   written (was not in the red-marked scope).
7. Verify: R. Reis first name / exact unit at U Bern for the final text; whether
   "Dr" or "Prof".
8. Page limit: B1 is max 10 pages. Re-check length after pasting — the expanded
   §1.2 and the new preliminary-results paragraph add ~half a page.
