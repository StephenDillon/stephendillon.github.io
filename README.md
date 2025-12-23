<style>
.hidden { display: none; }
table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
</style>

<div style="margin-bottom: 20px;">
  <div style="margin-bottom: 10px;">
    <strong>Language: </strong>
    <input type="radio" id="lang-en" name="lang" value="en" checked onchange="updateView()"> <label for="lang-en">English</label>
    <input type="radio" id="lang-it" name="lang" value="it" onchange="updateView()"> <label for="lang-it">Italiano</label>
  </div>
  <div>
    <strong>Units: </strong>
    <input type="radio" id="unit-mi" name="unit" value="mi" checked onchange="updateView()"> <label for="unit-mi">Miles</label>
    <input type="radio" id="unit-km" name="unit" value="km" onchange="updateView()"> <label for="unit-km">Kilometers</label>
  </div>
</div>

<table id="training-plan">
<thead><tr>
<th data-en="Week" data-it="Settimana">Week</th>
<th data-en="Date" data-it="Data">Date</th>
<th data-en="Workout Details" data-it="Dettagli Allenamento">Workout Details</th>
<th data-en="Distance" data-it="Distanza">Distance</th>
<th data-en="Target Pace" data-it="Ritmo Target">Target Pace</th>
</tr></thead><tbody>
<tr style="font-weight: bold;">
<td>1</td>
<td>Sun, Dec 28 2025</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="15"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Dec 29 2025</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Dec 30 2025</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 800m/400m active rec/800m (x4, 3' rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 800m/400m rec attivo/800m (x4, 3' rec) - Defaticamento">Warm-up - Strides - Intervals: 800m/400m active rec/800m (x4, 3' rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Dec 31 2025</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Jan 1 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Fri, Jan 2 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Sat, Jan 3 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="35.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>2</td>
<td>Sun, Jan 4 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="15"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Jan 5 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Jan 6 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 1k/0.5k active rec/1k (x3, 3' rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 1k/0.5k rec attivo/1k (x3, 3' rec) - Defaticamento">Warm-up - Strides - Intervals: 1k/0.5k active rec/1k (x3, 3' rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Jan 7 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Jan 8 2026</td>
<td><span class="lang-text" data-en="Hilly or Fartlek" data-it="Collinare o Fartlek">Hilly or Fartlek</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="lang-text" data-en="Variable / By Feel" data-it="Variabile / A Sensazione">Variable / By Feel</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Jan 9 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Jan 10 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="35.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>3</td>
<td>Sun, Jan 11 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="15"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Jan 12 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Jan 13 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 1k/0.5k rec/1k/0.5k rec/1k (x2, 3' rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 1k/0.5k rec/1k/0.5k rec/1k (x2, 3' rec) - Defaticamento">Warm-up - Strides - Intervals: 1k/0.5k rec/1k/0.5k rec/1k (x2, 3' rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="11"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Jan 14 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Jan 15 2026</td>
<td><span class="lang-text" data-en="Hilly or Fartlek" data-it="Collinare o Fartlek">Hilly or Fartlek</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="lang-text" data-en="Variable / By Feel" data-it="Variabile / A Sensazione">Variable / By Feel</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Jan 16 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Jan 17 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="36.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>4</td>
<td>Sun, Jan 18 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="17"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Jan 19 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Jan 20 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 1.5k-1k rec-1.5k (x2, 3' rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 1.5k-1k rec-1.5k (x2, 3' rec) - Defaticamento">Warm-up - Strides - Intervals: 1.5k-1k rec-1.5k (x2, 3' rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Jan 21 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Jan 22 2026</td>
<td><span class="lang-text" data-en="Hilly or Fartlek" data-it="Collinare o Fartlek">Hilly or Fartlek</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="lang-text" data-en="Variable / By Feel" data-it="Variabile / A Sensazione">Variable / By Feel</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Jan 23 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Jan 24 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="37.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>5</td>
<td>Sun, Jan 25 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="21"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Jan 26 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Jan 27 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - 2k - Intervals: 2k (x3, 2'30\" rec) - Cool-down" data-it="Riscaldamento - Allunghi - 2k - Ripetute: 2k (x3, 2'30\" rec) - Defaticamento">Warm-up - Strides - 2k - Intervals: 2k (x3, 2'30" rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Jan 28 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Jan 29 2026</td>
<td><span class="lang-text" data-en="Hilly or Fartlek" data-it="Collinare o Fartlek">Hilly or Fartlek</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="lang-text" data-en="Variable / By Feel" data-it="Variabile / A Sensazione">Variable / By Feel</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Jan 30 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Jan 31 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="41.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>6</td>
<td>Sun, Feb 1 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="26"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Feb 2 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Feb 3 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 2k (x4, 2'30\" rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 2k (x4, 2'30\" rec) - Defaticamento">Warm-up - Strides - Intervals: 2k (x4, 2'30" rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Feb 4 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Feb 5 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Feb 6 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Feb 7 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="46.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>7</td>
<td>Sun, Feb 8 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="24"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Feb 9 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Feb 10 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 3k (x3, 2'30\" rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 3k (x3, 2'30\" rec) - Defaticamento">Warm-up - Strides - Intervals: 3k (x3, 2'30" rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="11"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Feb 11 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Feb 12 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Feb 13 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Feb 14 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="45.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>8</td>
<td>Sun, Feb 15 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="30"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Feb 16 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Feb 17 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 3k (x4, 2'30\" rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 3k (x4, 2'30\" rec) - Defaticamento">Warm-up - Strides - Intervals: 3k (x4, 2'30" rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="14"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Feb 18 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Feb 19 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Feb 20 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Feb 21 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="54.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>9</td>
<td>Sun, Feb 22 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="27"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Feb 23 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Feb 24 2026</td>
<td><span class="lang-text" data-en="Warm-up - Strides - Intervals: 2k (x4, 2'30\" rec) - Cool-down" data-it="Riscaldamento - Allunghi - Ripetute: 2k (x4, 2'30\" rec) - Defaticamento">Warm-up - Strides - Intervals: 2k (x4, 2'30" rec) - Cool-down</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Wed, Feb 25 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Feb 26 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Feb 27 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Feb 28 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="47.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>10</td>
<td>Sun, Mar 1 2026</td>
<td><span class="lang-text" data-en="Long Run" data-it="Lungo">Long Run</span></td>
<td><span class="dist-val" data-km="35"></span></td>
<td><span class="pace-val" data-pace-km="6:00-6:10 min/km" data-pace-mi="9:39-9:55 min/mi">9:39-9:55 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Mar 2 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Mar 3 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Wed, Mar 4 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Mar 5 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Mar 6 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Mar 7 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="55.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>11</td>
<td>Sun, Mar 8 2026</td>
<td><span class="lang-text" data-en="Half Marathon Marathon Pace" data-it="Mezza Maratona ritmo maratona">Half Marathon Marathon Pace</span></td>
<td><span class="dist-val" data-km="21"></span></td>
<td><span class="pace-val" data-pace-km="5:40 min/km" data-pace-mi="9:07 min/mi">9:07 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Mar 9 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Mar 10 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Wed, Mar 11 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Mar 12 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="10"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Mar 13 2026</td>
<td><span class="lang-text" data-en="Core Stability or Functional" data-it="Core Stability o Functional">Core Stability or Functional</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Mar 14 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="41.0"></span></td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td>12</td>
<td>Sun, Mar 15 2026</td>
<td><span class="lang-text" data-en="Warm-up - 15 km Marathon Pace" data-it="Riscaldamento - 15 km ritmo maratona">Warm-up - 15 km Marathon Pace</span></td>
<td><span class="dist-val" data-km="14"></span></td>
<td><span class="pace-val" data-pace-km="5:40 min/km" data-pace-mi="9:07 min/mi">9:07 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Mon, Mar 16 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Tue, Mar 17 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="8"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Wed, Mar 18 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Thu, Mar 19 2026</td>
<td><span class="lang-text" data-en="Easy Run" data-it="Corsa Lenta">Easy Run</span></td>
<td><span class="dist-val" data-km="6"></span></td>
<td><span class="pace-val" data-pace-km="6:10-6:20 min/km" data-pace-mi="9:55-10:11 min/mi">9:55-10:11 min/mi</span></td>
</tr>
<tr>
<td></td>
<td>Fri, Mar 20 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Sat, Mar 21 2026</td>
<td><span class="lang-text" data-en="Rest" data-it="Riposo">Rest</span></td>
<td>-</td>
<td>-</td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td>Sun, Mar 22 2026</td>
<td><span class="lang-text" data-en="Run Rome The Marathon" data-it="Run Rome The Marathon">Run Rome The Marathon</span></td>
<td><span class="dist-val" data-km="42.195"></span></td>
<td><span class="pace-val" data-pace-km="5:40 min/km" data-pace-mi="9:07 min/mi">9:07 min/mi</span></td>
</tr>
<tr style="font-weight: bold;">
<td></td>
<td></td>
<td><span class="lang-text" data-en="Weekly Total" data-it="Totale Settimanale">Weekly Total</span></td>
<td><span class="dist-val" data-km="70.2"></span></td>
<td>-</td>
</tr>
</tbody></table>

<script>
function updateView() {
    const lang = document.querySelector('input[name="lang"]:checked').value;
    const unit = document.querySelector('input[name="unit"]:checked').value;
    
    // Update headers
    document.querySelectorAll('th[data-en]').forEach(th => {
        th.textContent = th.getAttribute('data-' + lang);
        if (th.getAttribute('data-en') === "Distance") {
            th.textContent += (unit === 'mi' ? ' (miles)' : ' (km)');
        }
    });
    
    // Update text
    document.querySelectorAll('.lang-text').forEach(el => {
        el.textContent = el.getAttribute('data-' + lang);
    });
    
    // Update distance
    document.querySelectorAll('.dist-val').forEach(el => {
        const km = parseFloat(el.getAttribute('data-km'));
        if (unit === 'mi') {
            const miles = (km * 0.621371).toFixed(1);
            el.textContent = miles;
        } else {
            el.textContent = km;
        }
    });
    
    // Update pace
    document.querySelectorAll('.pace-val').forEach(el => {
        el.textContent = el.getAttribute(unit === 'mi' ? 'data-pace-mi' : 'data-pace-km');
    });
}
// Init
window.onload = updateView;
</script>