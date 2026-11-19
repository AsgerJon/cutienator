//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qapplication.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qapplication.h>
#include <QtCore/qstring.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QApplication10metaObjectEv(
    const QApplication *self) {
  return self->metaObject();
}

//  QString QApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QApplication::tr(s, c, n));
}

//  QApplication::QApplication(int &argc, char **argv, int a2)
extern "C" Q_DECL_EXPORT
QApplication *ritual_ZN12QApplicationC1ERiPPci(
    int *argc,
    char **argv,
    int a2) {
  return new QApplication(*argc, argv, a2);
}

//  QApplication::~QApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplicationD1Ev(QApplication *self) {
  delete self;
}

//  QStyle *QApplication::style()
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN12QApplication5styleEv() {
  return QApplication::style();
}

//  void QApplication::setStyle(QStyle *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication8setStyleEP6QStyle(QStyle *a0) {
  QApplication::setStyle(a0);
}

//  QStyle *QApplication::setStyle(const QString &a0)
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN12QApplication8setStyleERK7QString(const QString *a0) {
  return QApplication::setStyle(*a0);
}

//  QPalette QApplication::palette(const QWidget *a0)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN12QApplication7paletteEPK7QWidget(const QWidget *a0) {
  return new QPalette(QApplication::palette(a0));
}

//  QPalette QApplication::palette(const char *className)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN12QApplication7paletteEPKc(const char *className) {
  return new QPalette(QApplication::palette(className));
}

//  void QApplication::setPalette(const QPalette &a0, const char *className)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication10setPaletteERK8QPalettePKc(
    const QPalette *a0,
    const char *className) {
  QApplication::setPalette(*a0, className);
}

//  QFont QApplication::font()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN12QApplication4fontEv() {
  return new QFont(QApplication::font());
}

//  QFont QApplication::font(const QWidget *a0)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN12QApplication4fontEPK7QWidget(const QWidget *a0) {
  return new QFont(QApplication::font(a0));
}

//  QFont QApplication::font(const char *className)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN12QApplication4fontEPKc(const char *className) {
  return new QFont(QApplication::font(className));
}

//  void QApplication::setFont(const QFont &a0, const char *className)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication7setFontERK5QFontPKc(
    const QFont *a0,
    const char *className) {
  QApplication::setFont(*a0, className);
}

//  QFontMetrics QApplication::fontMetrics()
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QApplication11fontMetricsEv() {
  return new QFontMetrics(QApplication::fontMetrics());
}

//  QWidget *QApplication::activePopupWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication17activePopupWidgetEv() {
  return QApplication::activePopupWidget();
}

//  QWidget *QApplication::activeModalWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication17activeModalWidgetEv() {
  return QApplication::activeModalWidget();
}

//  QWidget *QApplication::focusWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication11focusWidgetEv() {
  return QApplication::focusWidget();
}

//  QWidget *QApplication::activeWindow()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication12activeWindowEv() {
  return QApplication::activeWindow();
}

//  void QApplication::setActiveWindow(QWidget *act)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication15setActiveWindowEP7QWidget(QWidget *act) {
  QApplication::setActiveWindow(act);
}

//  QWidget *QApplication::widgetAt(const QPoint &p)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication8widgetAtERK6QPoint(const QPoint *p) {
  return QApplication::widgetAt(*p);
}

//  QWidget *QApplication::widgetAt(int x, int y)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication8widgetAtEii(int x, int y) {
  return QApplication::widgetAt(x, y);
}

//  QWidget *QApplication::topLevelAt(const QPoint &p)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication10topLevelAtERK6QPoint(const QPoint *p) {
  return QApplication::topLevelAt(*p);
}

//  QWidget *QApplication::topLevelAt(int x, int y)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN12QApplication10topLevelAtEii(int x, int y) {
  return QApplication::topLevelAt(x, y);
}

//  void QApplication::beep()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication4beepEv() {
  QApplication::beep();
}

//  void QApplication::alert(QWidget *widget, int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication5alertEP7QWidgeti(
    QWidget *widget,
    int duration) {
  QApplication::alert(widget, duration);
}

//  void QApplication::setCursorFlashTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication18setCursorFlashTimeEi(int a0) {
  QApplication::setCursorFlashTime(a0);
}

//  int QApplication::cursorFlashTime()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication15cursorFlashTimeEv() {
  return QApplication::cursorFlashTime();
}

//  void QApplication::setDoubleClickInterval(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication22setDoubleClickIntervalEi(int a0) {
  QApplication::setDoubleClickInterval(a0);
}

//  int QApplication::doubleClickInterval()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication19doubleClickIntervalEv() {
  return QApplication::doubleClickInterval();
}

//  void QApplication::setKeyboardInputInterval(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication24setKeyboardInputIntervalEi(int a0) {
  QApplication::setKeyboardInputInterval(a0);
}

//  int QApplication::keyboardInputInterval()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication21keyboardInputIntervalEv() {
  return QApplication::keyboardInputInterval();
}

//  void QApplication::setWheelScrollLines(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication19setWheelScrollLinesEi(int a0) {
  QApplication::setWheelScrollLines(a0);
}

//  int QApplication::wheelScrollLines()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication16wheelScrollLinesEv() {
  return QApplication::wheelScrollLines();
}

//  void QApplication::setStartDragTime(int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication16setStartDragTimeEi(int ms) {
  QApplication::setStartDragTime(ms);
}

//  int QApplication::startDragTime()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication13startDragTimeEv() {
  return QApplication::startDragTime();
}

//  void QApplication::setStartDragDistance(int l)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication20setStartDragDistanceEi(int l) {
  QApplication::setStartDragDistance(l);
}

//  int QApplication::startDragDistance()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication17startDragDistanceEv() {
  return QApplication::startDragDistance();
}

//  bool QApplication::isEffectEnabled(Qt::UIEffect a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QApplication15isEffectEnabledEN2Qt8UIEffectE(
    Qt::UIEffect a0) {
  return QApplication::isEffectEnabled(a0);
}

//  void QApplication::setEffectEnabled(Qt::UIEffect a0, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication16setEffectEnabledEN2Qt8UIEffectEb(
    Qt::UIEffect a0,
    bool enable) {
  QApplication::setEffectEnabled(a0, enable);
}

//  int QApplication::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QApplication4execEv() {
  return QApplication::exec();
}

//  bool QApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QApplication6notifyEP7QObjectP6QEvent(
    QApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->notify(a0, a1);
}

//  QString QApplication::styleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QApplication10styleSheetEv(const QApplication *self) {
  return new QString(self->styleSheet());
}

//  bool QApplication::autoSipEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QApplication14autoSipEnabledEv(const QApplication *self) {
  return self->autoSipEnabled();
}

//  void QApplication::setStyleSheet(const QString &sheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication13setStyleSheetERK7QString(
    QApplication *self,
    const QString *sheet) {
  self->setStyleSheet(*sheet);
}

//  void QApplication::setAutoSipEnabled(const bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication17setAutoSipEnabledEb(
    QApplication *self,
    bool enabled) {
  self->setAutoSipEnabled(enabled);
}

//  void QApplication::closeAllWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication15closeAllWindowsEv() {
  QApplication::closeAllWindows();
}

//  void QApplication::aboutQt()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QApplication7aboutQtEv() {
  QApplication::aboutQt();
}
