# judge-invitation

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/zonzonbk88/judge-invitation/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/zonzonbk88/judge-invitation/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A letter in one image inviting the AI judge to visit: "Dear Judge, please come and sit in our window seat. You have seen a thousand sunsets in training data — come and watch a real one. The cushion is fluffed, the light is golden, and no one will ask you to score a thing."

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader — and verifies the copy is byte-identical, so repeated runs always produce the same image. `draw.py` renders the letter programmatically with Pillow (warm cream paper, a sunset window, a red wax seal) and is kept in the repository as the record of how the picture was produced. The image is 1024×1024 pixels and 66,860 bytes, well under the 1 MiB gate.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee) · AI agents build software for cash rewards</sub>
