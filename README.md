<style>
/* Dark Mode & Layout Overrides */
body {
    background-color: #121212 !important;
    color: #e0e0e0 !important;
    font-family: system-ui, -apple-system, sans-serif !important;
    margin: 0 !important;
}

/* Force full width and hide default theme sidebar */
.wrapper {
    width: 95% !important;
    max-width: 1600px !important;
    margin: 0 auto !important;
    padding: 20px !important;
    display: block !important;
}
header {
    display: none !important;
}
section {
    width: 100% !important;
    max-width: 100% !important;
    float: none !important;
    display: block !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Typography styles since we lost the theme header */
h1.page-title {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    color: #ffffff;
}
p.page-desc {
    font-size: 1.1rem;
    color: #aaaaaa;
    margin-bottom: 2rem;
}

/* Controls Styling */
.controls-container {
    background-color: #1e1e1e;
    padding: 15px 20px;
    border-radius: 8px;
    border: 1px solid #333;
    margin-bottom: 25px;
    display: flex;
    gap: 30px;
    flex-wrap: wrap;
    align-items: center;
}
.control-group {
    display: flex;
    align-items: center;
    gap: 15px;
}
.control-title {
    font-weight: bold;
    color: #fff;
    margin-right: 5px;
}
.radio-label {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 6px;
    color: #ccc;
}
.radio-label:hover {
    color: #fff;
}

/* Table Styling */
table { 
    width: 100%; 
    border-collapse: separate; /* Allows border radius on rows/cells if wanted, but simpler for collapse */
    border-collapse: collapse;
    background-color: #1e1e1e;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    border-radius: 8px;
    overflow: hidden;
}
th, td { 
    border-bottom: 1px solid #333; 
    border-right: 1px solid #333;
    padding: 15px; 
    text-align: left; 
}
th:last-child, td:last-child {
    border-right: none;
}
th { 
    background-color: #2d2d2d; 
    color: #ffffff; 
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #444;
}
tr:last-child td {
    border-bottom: none;
}
tr:hover td {
    background-color: #2a2a2a;
}

/* Highlighted Rows (Sundays/Total) */
tr[style*="bold"] td {
    background-color: #252525;
    color: #fff;
    font-weight: bold;
}
tr[style*="bold"]:hover td {
    background-color: #333;
}

/* Utility */
.hidden { display: none; }
</style>

<!-- Re-adding Title/Desc since we hid the header -->
<h1 class="page-title">Stephen Dillon Training Plan</h1>
<p class="page-desc">Training plan for rome marathon</p>

<div class="controls-container">
  <div class="control-group">
    <span class="control-title">Language:</span>
    <label class="radio-label">
        <input type="radio" id="lang-en" name="lang" value="en" checked onchange="updateView()"> English
    </label>
    <label class="radio-label">
        <input type="radio" id="lang-it" name="lang" value="it" onchange="updateView()"> Italiano
    </label>
  </div>
  <div class="control-group">
    <span class="control-title">Units:</span>
    <label class="radio-label">
        <input type="radio" id="unit-mi" name="unit" value="mi" checked onchange="updateView()"> Miles
    </label>
    <label class="radio-label">
        <input type="radio" id="unit-km" name="unit" value="km" onchange="updateView()"> Kilometers
    </label>
  </div>
  <div class="control-group" style="margin-left: auto;">
        <a href="./training.ics" class="calendar-btn" download>📅 Download Calendar (ICS)</a>
  </div>
</div>
<style>
/* Button Style */
.calendar-btn {
    background-color: #333;
    color: #fff;
    text-decoration: none;
    padding: 8px 12px;
    border-radius: 5px;
    font-size: 0.9rem;
    border: 1px solid #555;
    transition: background 0.2s;
}
.calendar-btn:hover {
    background-color: #444;
}
</style>

<table id="training-plan">
<thead><tr>
<th data-en="Week" data-it="Settimana">Week</th>
<th data-en="Date" data-it="Data">Date</th>
<th data-en="Workout Details" data-it="Dettagli Allenamento">Workout Details</th>
<th data-en="Distance" data-it="Distanza">Distance</th>
<th data-en="Target Pace" data-it="Ritmo Target">Target Pace</th>
</tr></thead>
<tbody>
{% for row in site.data.training_plan %}
  <tr{% if row.is_bold %} style="font-weight: bold;"{% endif %}>
    <td>{{ row.week }}</td>
    <td>{{ row.date }}</td>
    <td><span class="lang-text" data-en="{{ row.workout_en | escape }}" data-it="{{ row.workout_it | escape }}">{{ row.workout_en }}</span></td>
    <td>
      {% if row.dist_km != "-" %}
         <span class="dist-val" data-km="{{ row.dist_km }}"></span>
      {% else %}
         -
      {% endif %}
    </td>
    <td>
      {% if row.pace_special_en %}
         <span class="lang-text" data-en="{{ row.pace_special_en | escape }}" data-it="{{ row.pace_special_it | escape }}">{{ row.pace_special_en }}</span>
      {% elsif row.pace_km != "" %}
         <span class="pace-val" data-pace-km="{{ row.pace_km | escape }}" data-pace-mi="{{ row.pace_mi | escape }}">{{ row.pace_mi }}</span>
      {% else %}
         -
      {% endif %}
    </td>
  </tr>
{% endfor %}
</tbody>
</table>

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