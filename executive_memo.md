# Collections Performance: Executive Memo

*Decision brief \| Analysis period: January--August 8, 2026*

## 1. What happened?

The available payment data does not show a consistent month-on-month
improvement in payment success rate. The rate was 69.84% in January,
peaked at 71.52% in February, and was 70.06% in July. August's observed
rate was 67.40%, but the dataset only runs through August 8 and should
not be compared directly with complete months.

## 2. What may explain the pattern?

Initial portfolio and targeting analyses show differences across risk
segments and communication channels, but they do not establish
causation. Targeting contact rates were broadly similar across channels
before July and from July onward. More analysis is needed to test
portfolio mix, campaign attribution, agent performance, and targeting
effects.

## 3. Data quality and confidence

The raw payment table contains 25,500 rows. Exact-row deduplication
removed 486 excess rows, leaving 25,014 rows. A separate exploratory
step retained one row per `payment_id`, resulting in 25,000 records;
this rule requires source-of-truth validation before adoption. After
that step, 368 payment references were missing and 2,043 payment records
had borrower IDs that did not match the borrower table. The accounts
table also had 455 missing borrower IDs and 2,458 non-missing borrower
IDs without a match. These issues reduce confidence in attribution and
linkage.

Confidence is moderate for the descriptive payment-success calculations
and low for conclusions about actual debt recovery, causal drivers, or
the reported 11% claim. Payment success rate is not equivalent to
recovery rate, which requires a validated recovery numerator and
portfolio denominator.

## 4. Recommended action and investment

Do not commit the full ₹10 Cr to a channel or operational intervention
based on the current evidence. Better borrower targeting is a reasonable
candidate to test, but its incremental recovery and ROI have not been
established. Run a controlled pilot that randomly assigns eligible
accounts to current targeting and improved targeting, stratified by
risk, DPD, loan type, and geography. Measure incremental cash recovered
per eligible account, net of reversals and intervention costs, over a
prespecified follow-up window.

## 5. Financial impact and next steps

A defensible estimate of incremental recovery, ROI, and break-even
cannot yet be calculated because the current analysis does not establish
a causal lift or validated cost per incremental rupee recovered. Before
investment, reconcile payment IDs and references, validate timestamps
and reversal handling, define the recovery denominator, and quantify
pilot costs. Scale only if the pilot's incremental recovery and downside
case meet a pre-agreed investment hurdle.

**Conclusion:** The available evidence does not substantiate the
reported 11% month-on-month improvement in actual recovery. It also does
not prove that the claim is false. Validate the recovery metric and run
a controlled experiment before committing the full investment.
