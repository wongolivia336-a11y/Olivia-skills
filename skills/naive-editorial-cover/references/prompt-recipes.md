# Prompt recipes｜生成时让笨拙变得可控

## 主Prompt（将方括号改为本次文章信息）
Draw a deliberately clumsy, human-made editorial doodle for a Chinese literary essay about [TOPIC]. The single visual metaphor is [SPECIFIC EVERYDAY OBJECTS + THEIR RELATIONSHIP]. Make it look as if a non-illustrator drew it slowly in MS Paint with a mouse: visibly uneven black outlines, slight pixel stair-steps, inconsistent line width, blunt corners, shaky hand-eye coordination, flat white or warm-white background, and one restrained indigo-blue accent (#4746C4). Use only 1–3 recognizable objects. Keep at least 40% quiet negative space and avoid text entirely. The metaphor should be legible in one glance yet a little awkward, intimate, and visually unresolved. 1080x460 horizontal composition, safe margins around important objects. Sharp bitmap edges; intentionally naive drawing, not low-resolution blur.

## 强制负面Prompt
No glossy AI illustration; no isometric 3D; no perfect vector Bézier outlines; no hand-lettering; no fake typography; no complex background; no excessive paper texture; no gradients, glow, floating particles, cinematic light, drop shadows, glass, plastic, stock symbols, robotic faces, circuit boards, decorative logos, multiple bright colors, random icons, collage overload, or overly sophisticated kawaii design. Do not reproduce any existing cover's specific subject or layout.

## 参考图转译
给出既有封面时，只提取线条的粗糙程度、背景留白、彩色比例和尺度关系；替换所有**主题物件**，以新文章的具体论证生成新隐喻。用户明确要求同一张图续改时才保留原物件。

## 一次迭代只动一个参数
- 太精致：减少曲线的平滑度和矢量对齐；加少量鼠标停顿点。
- 太脏：减噪、去纸纹，确保黑线清晰。
- 太多：减物件至1–3个，减少色块。
- 太抽象：换成现实中的可识别物品，并让物品之间有动作关系。
- 太像PPT插图：换回蓝紫与黑线，不用 naive-ppt 的橘红一色。
- 太像旧封面：换视觉隐喻，保留画法，不保留书/插座。

## 可迁移主题方向（非成稿）
- 艺术临摹与创新：两张重叠但没有完全对齐的纸。
- 城市感官：一个手绘路口和一条迟疑地绕开的路径。
- 数字记忆：一只画得不标准的抽屉，伸出来的纸条在边缘停住。
这些只是生成机制示意，不是固定配图库。
