---
case_id: waymo-commercial-robotaxis
organisation: Waymo
title: Commercial Autonomous Robotaxi Service
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.forbes.com/sites/nicolekobie/2025/09/25/waymo-wants-companies-to-off...
  url: https://www.forbes.com/sites/nicolekobie/2025/09/25/waymo-wants-companies-to-offer-robotaxis-as-corporate-perk/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.cnet.com/roadshow/news/waymo-adds-4-new-cities-to-its-roster-everyth...
  url: https://www.cnet.com/roadshow/news/waymo-adds-4-new-cities-to-its-roster-everything-to-know-about-the-robotaxi-service/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://techcrunch.com/2025/12/24/waymo-explains-why-its-robotaxis-got-stuck-dur...
  url: https://techcrunch.com/2025/12/24/waymo-explains-why-its-robotaxis-got-stuck-during-the-sf-blackout/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://www.wired.com/story/waymo-self-driving-taxi-service-launch-chandler-ariz...
  url: https://www.wired.com/story/waymo-self-driving-taxi-service-launch-chandler-arizona/
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Waymo provides over 10 million paid autonomous rides
  claim_description: Waymo has provided more than 10 million paid rides to customers
    using its autonomous vehicle technology across multiple cities.
  source_ids:
  - S2
  source_quote: The self-driving company says it's driven over 100 million fully autonomous
    miles on public roads and has provided more than 10 million paid rides.
  quote_location: Mid-article
  ai_attribution: direct
  attribution_evidence: The rides are provided directly by Waymo's autonomous driving
    technology (Waymo Driver) without human drivers in many deployments.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - business_growth
  cognitive_depth: autonomous
  metric_raw:
    value: '10000000'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-002
  claim_title: Waymo drives over 100 million fully autonomous miles on public roads
  claim_description: Waymo's autonomous vehicles have accumulated over 100 million
    miles of fully autonomous driving on public roads, demonstrating operational scale
    and reliability.
  source_ids:
  - S2
  source_quote: The self-driving company says it's driven over 100 million fully autonomous
    miles on public roads and has provided more than 10 million paid rides.
  quote_location: Mid-article
  ai_attribution: direct
  attribution_evidence: The autonomous miles are driven directly by Waymo's AI-powered
    self-driving system (Waymo Driver) without human intervention.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - business_growth
  cognitive_depth: autonomous
  metric_raw:
    value: '100000000'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-003
  claim_title: 88% reduction in crashes leading to serious injuries compared to human
    drivers
  claim_description: Over 71 million autonomous miles, Waymo Driver had 88% fewer
    crashes leading to serious injuries or worse compared to average human drivers
    over the same distance in operating cities.
  source_ids:
  - S2
  source_quote: over the course of 71 million autonomous miles driven through March
    2025, its Waymo Driver technology had 88% fewer crashes leading to serious injuries
    or worse...compared with an average human driver over the same distance in our
    operating cities.
  quote_location: Safety Impact report section
  ai_attribution: direct
  attribution_evidence: The safety improvement is directly attributed to Waymo Driver
    autonomous technology replacing human drivers.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '88'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-004
  claim_title: 78% reduction in injury-causing crashes compared to human drivers
  claim_description: Waymo Driver technology had 78% fewer injury-causing crashes
    compared to average human drivers over the same distance in operating cities.
  source_ids:
  - S2
  source_quote: its Waymo Driver technology had 88% fewer crashes leading to serious
    injuries or worse and 78% fewer injury-causing crashes, compared with an average
    human driver over the same distance in our operating cities.
  quote_location: Safety Impact report section
  ai_attribution: direct
  attribution_evidence: The reduction in injury-causing crashes is directly attributed
    to Waymo's autonomous driving technology replacing human drivers.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '78'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-005
  claim_title: 93% reduction in crashes with injuries to pedestrians
  claim_description: Waymo Driver reported 93% fewer crashes with injuries to pedestrians
    compared to average human drivers over the same distance.
  source_ids:
  - S2
  source_quote: It also reported significantly fewer crashes with injuries to pedestrians
    (93%), cyclists (81%) and motorcyclists (86%).
  quote_location: Safety Impact report section
  ai_attribution: direct
  attribution_evidence: The reduction in pedestrian injury crashes is directly attributed
    to Waymo's autonomous driving technology.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '93'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-006
  claim_title: 81% reduction in crashes with injuries to cyclists
  claim_description: Waymo Driver reported 81% fewer crashes with injuries to cyclists
    compared to average human drivers over the same distance.
  source_ids:
  - S2
  source_quote: It also reported significantly fewer crashes with injuries to pedestrians
    (93%), cyclists (81%) and motorcyclists (86%).
  quote_location: Safety Impact report section
  ai_attribution: direct
  attribution_evidence: The reduction in cyclist injury crashes is directly attributed
    to Waymo's autonomous driving technology.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '81'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-007
  claim_title: 86% reduction in crashes with injuries to motorcyclists
  claim_description: Waymo Driver reported 86% fewer crashes with injuries to motorcyclists
    compared to average human drivers over the same distance.
  source_ids:
  - S2
  source_quote: It also reported significantly fewer crashes with injuries to pedestrians
    (93%), cyclists (81%) and motorcyclists (86%).
  quote_location: Safety Impact report section
  ai_attribution: direct
  attribution_evidence: The reduction in motorcyclist injury crashes is directly attributed
    to Waymo's autonomous driving technology.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '86'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-008
  claim_title: Waymo successfully traversed over 7,000 dark signals during SF power
    outage
  claim_description: During a San Francisco power outage, Waymo's autonomous vehicles
    successfully navigated more than 7,000 disabled traffic signals, demonstrating
    operational resilience.
  source_ids:
  - S3
  source_quote: While a lot of focus has been placed on the instances where Waymo's
    robotaxis got stuck during the power outage, the company shared that its vehicles
    successfully traversed more than 7,000 dark signals on Saturday.
  quote_location: Near end of article
  ai_attribution: direct
  attribution_evidence: The autonomous navigation of disabled traffic signals was
    performed directly by Waymo's self-driving software treating them as four-way
    stops.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: autonomous
  metric_raw:
    value: '7000'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-009
  claim_title: One in six riders use Waymo robotaxis for commuting to work or school
  claim_description: Nearly one in six Waymo riders in San Francisco, LA, and Phoenix
    use the autonomous robotaxis to commute to work or school, demonstrating adoption
    for regular transportation needs.
  source_ids:
  - S1
  source_quote: Waymo saying that nearly one in six riders in those cities use the
    robotaxis to commute to work or school.
  quote_location: Early in article
  ai_attribution: direct
  attribution_evidence: The commuting service is provided directly by Waymo's autonomous
    vehicles, enabling workers and students to travel without driving.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: autonomous
  metric_raw:
    value: '16.67'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-010
  claim_title: Hundreds of thousands of trips to Phoenix Sky Harbor International
    Airport
  claim_description: Waymo has served hundreds of thousands of autonomous trips to
    and from Phoenix Sky Harbor International Airport, which remains the single most
    popular Waymo destination in Phoenix.
  source_ids:
  - S2
  source_quote: Waymo said in September 2025 that it has served hundreds of thousands
    of trips to/from Sky Harbor, and it remains the single most popular Waymo destination
    in Phoenix.
  quote_location: Phoenix section
  ai_attribution: direct
  attribution_evidence: The airport trips are provided directly by Waymo's fully autonomous
    vehicles without human drivers.
  verification_status: needs_review
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - business_growth
  cognitive_depth: autonomous
  metric_raw:
    value: hundreds of thousands
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-011
  claim_title: Waymo enables workers to work or relax during commute
  claim_description: By allowing workers to commute without driving, Waymo's autonomous
    vehicles enable passengers to work or relax during their journey, improving productivity
    and experience.
  source_ids:
  - S1
  source_quote: Waymo argued by allowing workers to commute without driving, they
    could work on the way — or relax, too.
  quote_location: Mid-article
  ai_attribution: direct
  attribution_evidence: The ability to work or relax is directly enabled by Waymo's
    autonomous driving technology eliminating the need for passengers to drive.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
  - velocity
  cognitive_depth: autonomous
  metric_raw: null
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-012
  claim_title: Waymo expands mobility access for those who cannot drive
  claim_description: Waymo's autonomous vehicles expand mobility access particularly
    for those in the community who can't drive or don't have access to a vehicle,
    improving transportation equity.
  source_ids:
  - S1
  source_quote: Embrace cutting-edge technology to expand mobility access, particularly
    for those in your community who can't drive or don't have access to a vehicle
  quote_location: Accessibility section
  ai_attribution: direct
  attribution_evidence: The expanded mobility access is directly enabled by Waymo's
    autonomous driving technology providing transportation without requiring passengers
    to drive.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: autonomous
  metric_raw: null
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Waymo is owned by Alphabet
  claim_description: Waymo is the autonomous vehicle division owned by Alphabet, Google's
    parent company.
  source_ids:
  - S1
  - S2
  source_quote: Waymo, the autonomous arm of Google's parent, Alphabet
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-002
  context_type: sectoral
  claim_title: Waymo operates in autonomous transportation/mobility sector
  claim_description: Waymo operates in the autonomous vehicle and ride-hailing transportation
    sector, providing robotaxi services.
  source_ids:
  - S1
  - S2
  source_quote: Driverless robotaxis aren't just for private individuals
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-003
  context_type: products_services
  claim_title: Waymo One commercial robotaxi service
  claim_description: Waymo operates Waymo One, a commercial autonomous ride-hailing
    service available to the general public in multiple cities.
  source_ids:
  - S2
  - S4
  source_quote: Today, we're taking the next step in our journey with the introduction
    of our commercial self-driving service, Waymo One
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-004
  context_type: products_services
  claim_title: Waymo for Business corporate service
  claim_description: Waymo launched Waymo for Business, a corporate account service
    allowing businesses to offer autonomous rides as employee perks or for business
    travel.
  source_ids:
  - S1
  source_quote: It's newly launched Waymo for Business is similar to setting up a
    corporate account with Uber or your local cab company
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-005
  context_type: scale
  claim_title: Waymo operates in 9+ US cities with commercial service
  claim_description: Waymo offers fully autonomous rides to the general public in
    Phoenix, San Francisco, Los Angeles, Atlanta, and Austin, with expansion to additional
    cities underway.
  source_ids:
  - S2
  source_quote: Waymo currently offers fully autonomous rides to the general public
    in Phoenix, San Francisco, Los Angeles, Atlanta, and Austin, Texas
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-006
  context_type: scale
  claim_title: Waymo operates 24/7 service in multiple cities
  claim_description: Waymo's robotaxi service operates 24 hours a day, seven days
    a week in cities like Phoenix, San Francisco, and Los Angeles.
  source_ids:
  - S2
  source_quote: The service operates 24 hours a day, seven days a week.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-007
  context_type: scale
  claim_title: Waymo fleet includes 1,500+ vehicles with 2,000 more planned
  claim_description: Waymo operates a fleet of approximately 1,500 fully autonomous
    Jaguar I-Pace vehicles, with plans to add 2,000 more vehicles.
  source_ids:
  - S2
  source_quote: The plan is to add 2,000 more fully autonomous Jaguar I-Pace vehicles
    to its existing 1,500-vehicle fleet.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-008
  context_type: temporal
  claim_title: Phoenix service launched in 2020
  claim_description: Phoenix was the first city where Waymo opened fully autonomous
    rides to the public in 2020.
  source_ids:
  - S2
  source_quote: Phoenix was the first city to open up fully autonomous Waymo rides
    to the public, in 2020.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-009
  context_type: temporal
  claim_title: San Francisco service launched in late 2022
  claim_description: Waymo rolled out fully autonomous rides in San Francisco in late
    2022, following Phoenix.
  source_ids:
  - S2
  source_quote: San Francisco followed suit after Phoenix, rolling out fully autonomous
    rides in late 2022.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-010
  context_type: strategic_intent
  claim_title: Waymo pursuing commercial expansion strategy
  claim_description: Waymo is entering a new chapter and accelerating its commercial
    expansion to additional cities across the US.
  source_ids:
  - S2
  source_quote: In an Aug. 29 blog post, Waymo noted it's entering a new chapter and
    accelerating our commercial expansion.
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-011
  context_type: organisational
  claim_title: Partnership with Uber for ride-hailing integration
  claim_description: Waymo has partnered with Uber to integrate autonomous rides into
    the Uber app in cities like Austin and Atlanta.
  source_ids:
  - S2
  source_quote: You can also use the Uber app to summon one of Waymo's vehicles in
    Phoenix.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-012
  context_type: organisational
  claim_title: Partnership with Hyundai for next-generation vehicles
  claim_description: Waymo announced a partnership with Hyundai to bring next-generation
    autonomous technology into Ioniq 5 SUVs.
  source_ids:
  - S2
  source_quote: Last October, Waymo also announced it's partnering with Hyundai to
    bring the next generation of its technology into Ioniq 5 SUVs.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-013
  context_type: scale
  claim_title: Waymo operates across 260+ square miles in San Francisco Bay Area
  claim_description: Waymo's service area in the San Francisco Bay Area stretches
    across more than 260 square miles.
  source_ids:
  - S2
  source_quote: In November, Waymo expanded its service area to stretch across more
    than 260 square miles of the San Francisco Bay Area
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-014
  context_type: scale
  claim_title: Waymo operates across 120 square miles in Los Angeles County
  claim_description: Waymo's service covers nearly 120 square miles of LA County,
    including multiple neighborhoods and cities.
  source_ids:
  - S2
  source_quote: Now any interested passengers can hop in the robotaxis 24/7 and ride
    across nearly 120 square miles of LA County
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-015
  context_type: scale
  claim_title: Waymo operates across 90 square miles in Austin
  claim_description: Waymo's service in Austin covers 90 square miles with more than
    100 vehicles.
  source_ids:
  - S2
  source_quote: Riders can hail a Waymo across 90 square miles of Austin, including
    neighborhoods like Crestview, Windsor Park and Franklin Park
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-016
  context_type: temporal
  claim_title: Waymo started as Google's self-driving car project a decade ago
  claim_description: Waymo originated as Google's self-driving car project approximately
    a decade before the 2018 commercial launch.
  source_ids:
  - S4
  source_quote: In the decade since it started out as Google's self-driving car project,
    Waymo has made astounding progress.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-017
  context_type: scale
  claim_title: Waymo has driven 10 billion miles in simulation
  claim_description: In addition to real-world miles, Waymo has driven 10 billion
    miles in simulation for testing and development.
  source_ids:
  - S4
  source_quote: Its cars have driven 10 million miles on public roads in 25 US cities,
    and another 10 billion in simulation.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-018
  context_type: functional
  claim_title: Waymo for Business includes fleet management portal
  claim_description: Companies can manage robotaxi use via a business portal with
    reporting tools to set and track budget and monitor ride activity.
  source_ids:
  - S1
  source_quote: Companies can manage robo-ridehailing via a business portal with reporting
    tools to set and track budget and monitor ride activity.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10.0'
  apqc_name: Manage Enterprise Information
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-019
  context_type: scale
  claim_title: Waymo operates at two major international airports
  claim_description: Waymo provides autonomous rides at Phoenix Sky Harbor International
    Airport and San Jose Mineta International Airport.
  source_ids:
  - S2
  source_quote: Riders can now hail a driverless ride to San Jose Mineta International
    Airport, making it the second international airport at which Waymo operates, after
    Phoenix Sky Harbor International Airport.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-020
  context_type: organisational
  claim_title: Waymo operates 239,000 sq ft manufacturing facility in Phoenix
  claim_description: Waymo opened a new 239,000-square-foot autonomous vehicle factory
    in the Phoenix area for vehicle production.
  source_ids:
  - S2
  source_quote: In May, the company said it's opening a new, 239,000-square-foot autonomous
    vehicle factory in the Phoenix area.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
verification_summary:
  value_claims:
    total: 12
    verified: 8
    needs_review: 4
    rejected: 0
    by_attribution:
      direct: 12
  context_claims:
    total: 20
    verified: 18
    unverified: 2
    inferred: 0
  all_value_verified: false
  all_context_verified: false
human_validation_summary: null
status: needs_review
confidence: high
review_flags: []
ontology_metadata:
  version_used: '1.0'
  tagged_date: '2026-01-29'
  needs_retagging: false
---

# Commercial Autonomous Robotaxi Service

## Executive Summary

Waymo: Waymo provides over 10 million paid autonomous rides.

## Key Findings

- **Waymo provides over 10 million paid autonomous rides** — verified (adoption)
  - Quote: "The self-driving company says it's driven over 100 million fully autonomous miles on public roads and has provided more than 10 million paid rides."

- **Waymo drives over 100 million fully autonomous miles on public roads** — verified (adoption)
  - Quote: "The self-driving company says it's driven over 100 million fully autonomous miles on public roads and has provided more than 10 million paid rides."

- **88% reduction in crashes leading to serious injuries compared to human drivers** — needs_review (outcome)
  - Quote: "over the course of 71 million autonomous miles driven through March 2025, its Waymo Driver technology had 88% fewer crashes leading to serious injuries or worse...compared with an average human driver..."

- **78% reduction in injury-causing crashes compared to human drivers** — needs_review (outcome)
  - Quote: "its Waymo Driver technology had 88% fewer crashes leading to serious injuries or worse and 78% fewer injury-causing crashes, compared with an average human driver over the same distance in our operati..."

- **93% reduction in crashes with injuries to pedestrians** — verified (outcome)
  - Quote: "It also reported significantly fewer crashes with injuries to pedestrians (93%), cyclists (81%) and motorcyclists (86%)."

- **81% reduction in crashes with injuries to cyclists** — verified (outcome)
  - Quote: "It also reported significantly fewer crashes with injuries to pedestrians (93%), cyclists (81%) and motorcyclists (86%)."

- **86% reduction in crashes with injuries to motorcyclists** — verified (outcome)
  - Quote: "It also reported significantly fewer crashes with injuries to pedestrians (93%), cyclists (81%) and motorcyclists (86%)."

- **Waymo successfully traversed over 7,000 dark signals during SF power outage** — needs_review (outcome)
  - Quote: "While a lot of focus has been placed on the instances where Waymo's robotaxis got stuck during the power outage, the company shared that its vehicles successfully traversed more than 7,000 dark signal..."

- **One in six riders use Waymo robotaxis for commuting to work or school** — verified (adoption)
  - Quote: "Waymo saying that nearly one in six riders in those cities use the robotaxis to commute to work or school."

- **Hundreds of thousands of trips to Phoenix Sky Harbor International Airport** — needs_review (adoption)
  - Quote: "Waymo said in September 2025 that it has served hundreds of thousands of trips to/from Sky Harbor, and it remains the single most popular Waymo destination in Phoenix."

- **Waymo enables workers to work or relax during commute** — verified (method)
  - Quote: "Waymo argued by allowing workers to commute without driving, they could work on the way — or relax, too."

- **Waymo expands mobility access for those who cannot drive** — verified (method)
  - Quote: "Embrace cutting-edge technology to expand mobility access, particularly for those in your community who can't drive or don't have access to a vehicle"

## Sources

- **S1**: https://www.forbes.com/sites/nicolekobie/2025/09/25/waymo-wants-companies-to-offer-robotaxis-as-corporate-perk/
- **S2**: https://www.cnet.com/roadshow/news/waymo-adds-4-new-cities-to-its-roster-everything-to-know-about-the-robotaxi-service/
- **S3**: https://techcrunch.com/2025/12/24/waymo-explains-why-its-robotaxis-got-stuck-during-the-sf-blackout/
- **S4**: https://www.wired.com/story/waymo-self-driving-taxi-service-launch-chandler-arizona/
