class HebrewEventsCard extends HTMLElement {

  set hass(hass) {
    const entities = Object.values(hass.states)
      .filter(e => e.entity_id.includes("hebrew_events"));

    this.innerHTML = `
      <ha-card header="אירועים עבריים">
        <div style="padding:16px">
          ${entities.map(e => `
            <div style="margin-bottom:8px">
              ${e.attributes.friendly_name}
              <b>${e.state === "on" ? "🔥 היום!" : ""}</b>
            </div>
          `).join("")}
          <mwc-button @click=${() => this._add()}>
            הוסף אירוע
          </mwc-button>
        </div>
      </ha-card>
    `;
  }

  _add() {
    alert("הוספה דרך Settings > Services");
  }
}