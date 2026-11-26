//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstylehints.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qstylehints.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>

//  const QMetaObject *QStyleHints::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QStyleHints10metaObjectEv(
    const QStyleHints *self) {
  return self->metaObject();
}

//  void *QStyleHints::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QStyleHints11qt_metacastEPKc(
    QStyleHints *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QStyleHints::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QStyleHints11qt_metacallEN11QMetaObject4CallEiPPv(
    QStyleHints *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QStyleHints::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QStyleHints2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyleHints::tr(s, c, n));
}

//  QStyleHintsPrivate *QStyleHints::d_func()
extern "C" Q_DECL_EXPORT
QStyleHintsPrivate *ritual_ZN11QStyleHints6d_funcEv(QStyleHints *self) {
  return self->d_func();
}

//  const QStyleHintsPrivate *QStyleHints::d_func() const
extern "C" Q_DECL_EXPORT
const QStyleHintsPrivate *ritual_ZNK11QStyleHints6d_funcEv(
    const QStyleHints *self) {
  return self->d_func();
}

//  void QStyleHints::setMouseDoubleClickInterval(int
//      mouseDoubleClickInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints27setMouseDoubleClickIntervalEi(
    QStyleHints *self,
    int mouseDoubleClickInterval) {
  self->setMouseDoubleClickInterval(mouseDoubleClickInterval);
}

//  int QStyleHints::mouseDoubleClickInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24mouseDoubleClickIntervalEv(
    const QStyleHints *self) {
  return self->mouseDoubleClickInterval();
}

//  int QStyleHints::mouseDoubleClickDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24mouseDoubleClickDistanceEv(
    const QStyleHints *self) {
  return self->mouseDoubleClickDistance();
}

//  int QStyleHints::touchDoubleTapDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints22touchDoubleTapDistanceEv(
    const QStyleHints *self) {
  return self->touchDoubleTapDistance();
}

//  void QStyleHints::setMousePressAndHoldInterval(int
//      mousePressAndHoldInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints28setMousePressAndHoldIntervalEi(
    QStyleHints *self,
    int mousePressAndHoldInterval) {
  self->setMousePressAndHoldInterval(mousePressAndHoldInterval);
}

//  int QStyleHints::mousePressAndHoldInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints25mousePressAndHoldIntervalEv(
    const QStyleHints *self) {
  return self->mousePressAndHoldInterval();
}

//  void QStyleHints::setStartDragDistance(int startDragDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints20setStartDragDistanceEi(
    QStyleHints *self,
    int startDragDistance) {
  self->setStartDragDistance(startDragDistance);
}

//  int QStyleHints::startDragDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17startDragDistanceEv(const QStyleHints *self) {
  return self->startDragDistance();
}

//  void QStyleHints::setStartDragTime(int startDragTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints16setStartDragTimeEi(
    QStyleHints *self,
    int startDragTime) {
  self->setStartDragTime(startDragTime);
}

//  int QStyleHints::startDragTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints13startDragTimeEv(const QStyleHints *self) {
  return self->startDragTime();
}

//  int QStyleHints::startDragVelocity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17startDragVelocityEv(const QStyleHints *self) {
  return self->startDragVelocity();
}

//  void QStyleHints::setKeyboardInputInterval(int keyboardInputInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints24setKeyboardInputIntervalEi(
    QStyleHints *self,
    int keyboardInputInterval) {
  self->setKeyboardInputInterval(keyboardInputInterval);
}

//  int QStyleHints::keyboardInputInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints21keyboardInputIntervalEv(
    const QStyleHints *self) {
  return self->keyboardInputInterval();
}

#if QT_DEPRECATED_SINCE(6, 5)
//  int QStyleHints::keyboardAutoRepeatRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints22keyboardAutoRepeatRateEv(
    const QStyleHints *self) {
  return self->keyboardAutoRepeatRate();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  qreal QStyleHints::keyboardAutoRepeatRateF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QStyleHints23keyboardAutoRepeatRateFEv(
    const QStyleHints *self) {
  return self->keyboardAutoRepeatRateF();
}

//  void QStyleHints::setCursorFlashTime(int cursorFlashTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints18setCursorFlashTimeEi(
    QStyleHints *self,
    int cursorFlashTime) {
  self->setCursorFlashTime(cursorFlashTime);
}

//  int QStyleHints::cursorFlashTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints15cursorFlashTimeEv(const QStyleHints *self) {
  return self->cursorFlashTime();
}

//  bool QStyleHints::showIsFullScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints16showIsFullScreenEv(const QStyleHints *self) {
  return self->showIsFullScreen();
}

//  bool QStyleHints::showIsMaximized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints15showIsMaximizedEv(const QStyleHints *self) {
  return self->showIsMaximized();
}

//  bool QStyleHints::showShortcutsInContextMenus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints27showShortcutsInContextMenusEv(
    const QStyleHints *self) {
  return self->showShortcutsInContextMenus();
}

//  void QStyleHints::setShowShortcutsInContextMenus(bool
//      showShortcutsInContextMenus)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints30setShowShortcutsInContextMenusEb(
    QStyleHints *self,
    bool showShortcutsInContextMenus) {
  self->setShowShortcutsInContextMenus(showShortcutsInContextMenus);
}

//  Qt::ContextMenuTrigger QStyleHints::contextMenuTrigger() const
extern "C" Q_DECL_EXPORT
Qt::ContextMenuTrigger ritual_ZNK11QStyleHints18contextMenuTriggerEv(
    const QStyleHints *self) {
  return self->contextMenuTrigger();
}

//  void QStyleHints::setContextMenuTrigger(Qt::ContextMenuTrigger
//      contextMenuTrigger)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints21setContextMenuTriggerEN2Qt18ContextMenuTriggerE(
    QStyleHints *self,
    Qt::ContextMenuTrigger contextMenuTrigger) {
  self->setContextMenuTrigger(contextMenuTrigger);
}

//  bool QStyleHints::menuSelectionWraps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints18menuSelectionWrapsEv(const QStyleHints *self) {
  return self->menuSelectionWraps();
}

//  int QStyleHints::passwordMaskDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints17passwordMaskDelayEv(const QStyleHints *self) {
  return self->passwordMaskDelay();
}

//  QChar QStyleHints::passwordMaskCharacter() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK11QStyleHints21passwordMaskCharacterEv(
    const QStyleHints *self) {
  return new QChar(self->passwordMaskCharacter());
}

//  qreal QStyleHints::fontSmoothingGamma() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QStyleHints18fontSmoothingGammaEv(
    const QStyleHints *self) {
  return self->fontSmoothingGamma();
}

//  bool QStyleHints::useRtlExtensions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints16useRtlExtensionsEv(const QStyleHints *self) {
  return self->useRtlExtensions();
}

//  bool QStyleHints::setFocusOnTouchRelease() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints22setFocusOnTouchReleaseEv(
    const QStyleHints *self) {
  return self->setFocusOnTouchRelease();
}

//  Qt::TabFocusBehavior QStyleHints::tabFocusBehavior() const
extern "C" Q_DECL_EXPORT
Qt::TabFocusBehavior ritual_ZNK11QStyleHints16tabFocusBehaviorEv(
    const QStyleHints *self) {
  return self->tabFocusBehavior();
}

//  void QStyleHints::setTabFocusBehavior(Qt::TabFocusBehavior
//      tabFocusBehavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints19setTabFocusBehaviorEN2Qt16TabFocusBehaviorE(
    QStyleHints *self,
    Qt::TabFocusBehavior tabFocusBehavior) {
  self->setTabFocusBehavior(tabFocusBehavior);
}

//  bool QStyleHints::singleClickActivation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints21singleClickActivationEv(
    const QStyleHints *self) {
  return self->singleClickActivation();
}

//  bool QStyleHints::useHoverEffects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStyleHints15useHoverEffectsEv(const QStyleHints *self) {
  return self->useHoverEffects();
}

//  void QStyleHints::setUseHoverEffects(bool useHoverEffects)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints18setUseHoverEffectsEb(
    QStyleHints *self,
    bool useHoverEffects) {
  self->setUseHoverEffects(useHoverEffects);
}

//  int QStyleHints::wheelScrollLines() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints16wheelScrollLinesEv(const QStyleHints *self) {
  return self->wheelScrollLines();
}

//  void QStyleHints::setWheelScrollLines(int scrollLines)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints19setWheelScrollLinesEi(
    QStyleHints *self,
    int scrollLines) {
  self->setWheelScrollLines(scrollLines);
}

//  void QStyleHints::setMouseQuickSelectionThreshold(int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints31setMouseQuickSelectionThresholdEi(
    QStyleHints *self,
    int threshold) {
  self->setMouseQuickSelectionThreshold(threshold);
}

//  int QStyleHints::mouseQuickSelectionThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints28mouseQuickSelectionThresholdEv(
    const QStyleHints *self) {
  return self->mouseQuickSelectionThreshold();
}

//  Qt::ColorScheme QStyleHints::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK11QStyleHints11colorSchemeEv(
    const QStyleHints *self) {
  return self->colorScheme();
}

//  void QStyleHints::setColorScheme(Qt::ColorScheme scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints14setColorSchemeEN2Qt11ColorSchemeE(
    QStyleHints *self,
    Qt::ColorScheme scheme) {
  self->setColorScheme(scheme);
}

//  void QStyleHints::unsetColorScheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints16unsetColorSchemeEv(QStyleHints *self) {
  self->unsetColorScheme();
}

//  const QAccessibilityHints *QStyleHints::accessibility() const
extern "C" Q_DECL_EXPORT
const QAccessibilityHints *ritual_ZNK11QStyleHints13accessibilityEv(
    const QStyleHints *self) {
  return self->accessibility();
}

//  std::chrono::milliseconds QStyleHints::toolTipWakeUpDelay() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK11QStyleHints18toolTipWakeUpDelayEv(
    const QStyleHints *self) {
  return static_cast<long long>(self->toolTipWakeUpDelay().count());
}

//  void QStyleHints::setToolTipWakeUpDelay(std::chrono::milliseconds
//      toolTipWakeUpDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints21setToolTipWakeUpDelayENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QStyleHints *self,
    long long toolTipWakeUpDelay) {
  self->setToolTipWakeUpDelay(std::chrono::milliseconds(toolTipWakeUpDelay));
}

//  int QStyleHints::toolTipWakeUpDelayAsMSec() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QStyleHints24toolTipWakeUpDelayAsMSecEv(
    const QStyleHints *self) {
  return self->toolTipWakeUpDelayAsMSec();
}

//  void QStyleHints::cursorFlashTimeChanged(int cursorFlashTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints22cursorFlashTimeChangedEi(
    QStyleHints *self,
    int cursorFlashTime) {
  self->cursorFlashTimeChanged(cursorFlashTime);
}

//  void QStyleHints::keyboardInputIntervalChanged(int keyboardInputInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints28keyboardInputIntervalChangedEi(
    QStyleHints *self,
    int keyboardInputInterval) {
  self->keyboardInputIntervalChanged(keyboardInputInterval);
}

//  void QStyleHints::mouseDoubleClickIntervalChanged(int
//      mouseDoubleClickInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints31mouseDoubleClickIntervalChangedEi(
    QStyleHints *self,
    int mouseDoubleClickInterval) {
  self->mouseDoubleClickIntervalChanged(mouseDoubleClickInterval);
}

//  void QStyleHints::mousePressAndHoldIntervalChanged(int
//      mousePressAndHoldInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints32mousePressAndHoldIntervalChangedEi(
    QStyleHints *self,
    int mousePressAndHoldInterval) {
  self->mousePressAndHoldIntervalChanged(mousePressAndHoldInterval);
}

//  void QStyleHints::startDragDistanceChanged(int startDragDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints24startDragDistanceChangedEi(
    QStyleHints *self,
    int startDragDistance) {
  self->startDragDistanceChanged(startDragDistance);
}

//  void QStyleHints::startDragTimeChanged(int startDragTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints20startDragTimeChangedEi(
    QStyleHints *self,
    int startDragTime) {
  self->startDragTimeChanged(startDragTime);
}

//  void QStyleHints::tabFocusBehaviorChanged(Qt::TabFocusBehavior
//      tabFocusBehavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints23tabFocusBehaviorChangedEN2Qt16TabFocusBehaviorE(
    QStyleHints *self,
    Qt::TabFocusBehavior tabFocusBehavior) {
  self->tabFocusBehaviorChanged(tabFocusBehavior);
}

//  void QStyleHints::useHoverEffectsChanged(bool useHoverEffects)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints22useHoverEffectsChangedEb(
    QStyleHints *self,
    bool useHoverEffects) {
  self->useHoverEffectsChanged(useHoverEffects);
}

//  void QStyleHints::showShortcutsInContextMenusChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints34showShortcutsInContextMenusChangedEb(
    QStyleHints *self,
    bool a0) {
  self->showShortcutsInContextMenusChanged(a0);
}

//  void QStyleHints::contextMenuTriggerChanged(Qt::ContextMenuTrigger
//      contextMenuTrigger)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints25contextMenuTriggerChangedEN2Qt18ContextMenuTriggerE(
    QStyleHints *self,
    Qt::ContextMenuTrigger contextMenuTrigger) {
  self->contextMenuTriggerChanged(contextMenuTrigger);
}

//  void QStyleHints::wheelScrollLinesChanged(int scrollLines)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints23wheelScrollLinesChangedEi(
    QStyleHints *self,
    int scrollLines) {
  self->wheelScrollLinesChanged(scrollLines);
}

//  void QStyleHints::mouseQuickSelectionThresholdChanged(int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints35mouseQuickSelectionThresholdChangedEi(
    QStyleHints *self,
    int threshold) {
  self->mouseQuickSelectionThresholdChanged(threshold);
}

//  void QStyleHints::colorSchemeChanged(Qt::ColorScheme colorScheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints18colorSchemeChangedEN2Qt11ColorSchemeE(
    QStyleHints *self,
    Qt::ColorScheme colorScheme) {
  self->colorSchemeChanged(colorScheme);
}

//  void QStyleHints::toolTipWakeUpDelayChanged(std::chrono::milliseconds
//      toolTipWakeUpDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints25toolTipWakeUpDelayChangedENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QStyleHints *self,
    long long toolTipWakeUpDelay) {
  self->toolTipWakeUpDelayChanged(
      std::chrono::milliseconds(toolTipWakeUpDelay));
}

//  void QStyleHints::toolTipWakeUpDelayAsMSecChanged(int toolTipWakeUpDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStyleHints31toolTipWakeUpDelayAsMSecChangedEi(
    QStyleHints *self,
    int toolTipWakeUpDelay) {
  self->toolTipWakeUpDelayAsMSecChanged(toolTipWakeUpDelay);
}

//  QStyleHints::QStyleHints()
extern "C" Q_DECL_EXPORT
QStyleHints *ritual_ZN11QStyleHintsC1Ev() {
  return new QStyleHints();
}
