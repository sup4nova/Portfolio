<template>
  <!-- défs globales (#spark, #star, #torn, #clip-flower) — monté une seule fois dans App.vue -->
  <svg width="0" height="0" style="position: absolute" aria-hidden="true" focusable="false">
    <defs>
      <symbol id="spark" viewBox="-12 -12 24 24">
        <path d="M0-11.5C.9-4 4-1 11.5 0 4 1 .9 4 0 11.5-.9 4-4 1-11.5 0-4-1-.9-4 0-11.5Z" fill="currentColor" />
      </symbol>
      <symbol id="star" viewBox="-100 -100 200 200" overflow="visible">
        <path
          d="M 3.19,-82.52 L 19.88,-32.91 Q 21.15,-29.12 25.15,-29.08 L 77.52,-28.53 Q 87.52,-28.43 79.49,-22.47 L 37.45,8.74 Q 34.24,11.12 35.44,14.94 L 51.11,64.89 Q 54.10,74.43 45.95,68.64 L 3.26,38.32 Q 0,36 -3.26,38.32 L -45.95,68.64 Q -54.10,74.43 -51.11,64.89 L -35.44,14.94 Q -34.24,11.12 -37.45,8.74 L -79.49,-22.47 Q -87.52,-28.43 -77.52,-28.53 L -25.15,-29.08 Q -21.15,-29.12 -19.88,-32.91 L -3.19,-82.52 Q 0,-92 3.19,-82.52 Z"
          fill="currentColor"
          stroke="#1d4a52"
          stroke-width="8"
          stroke-linejoin="round"
        />
      </symbol>
      <symbol id="torn" viewBox="0 0 1200 34" preserveAspectRatio="none">
        <path d="M0 0H1200V12L1160 18L1120 8L1080 16L1040 10L1000 20L960 9L920 16L880 7L840 17L800 11L760 20L720 8L680 15L640 10L600 19L560 7L520 16L480 11L440 20L400 9L360 15L320 7L280 17L240 10L200 19L160 8L120 16L80 9L40 17L0 12Z" />
      </symbol>
      <clipPath id="clip-flower" clipPathUnits="objectBoundingBox">
        <circle cx=".5" cy=".5" r=".33" />
        <circle cx=".8" cy=".5" r=".2" />
        <circle cx=".712" cy=".712" r=".2" />
        <circle cx=".5" cy=".8" r=".2" />
        <circle cx=".288" cy=".712" r=".2" />
        <circle cx=".2" cy=".5" r=".2" />
        <circle cx=".288" cy=".288" r=".2" />
        <circle cx=".5" cy=".2" r=".2" />
        <circle cx=".712" cy=".288" r=".2" />
      </clipPath>
    </defs>
  </svg>
</template>
