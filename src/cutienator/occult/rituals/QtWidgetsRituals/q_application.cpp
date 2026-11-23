//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qapplication.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qapplication.h>
#include <QtCore/qstring.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QApplication may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQApplication : QApplication {
  using QApplication::event;
};

//  A QApplication that Python can take functions over in. Every QApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQApplicationCall0)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQApplicationCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQApplicationCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQApplicationCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQApplicationCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQApplicationCall5)(const void *, QEvent *, int *);
typedef void (*CuteQApplicationCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQApplicationCall7)(const void *, const QMetaMethod *, int *);
class CuteQApplication : public QApplication {
public:
  using QApplication::QApplication;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QCoreApplication6notifyEP7QObjectP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool QApplication::notify(QObject *a0, QEvent *a1)
  bool notify(QObject *a0, QEvent *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQApplicationCall0 call = reinterpret_cast<CuteQApplicationCall0>(taken[0]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QApplication::notify(a0, a1);
  }

  //  bool QApplication::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQApplicationCall1 call = reinterpret_cast<CuteQApplicationCall1>(taken[1]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QApplication::event(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQApplicationCall2 call = reinterpret_cast<CuteQApplicationCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQApplicationCall3 call = reinterpret_cast<CuteQApplicationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQApplicationCall4 call = reinterpret_cast<CuteQApplicationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQApplicationCall5 call = reinterpret_cast<CuteQApplicationCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQApplicationCall6 call = reinterpret_cast<CuteQApplicationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQApplicationCall7 call = reinterpret_cast<CuteQApplicationCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

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
  return new CuteQApplication(*argc, argv, a2);
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

//  QWidgetList QApplication::allWidgets()
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN12QApplication10allWidgetsEv() {
  return new QList<QWidget *>(QApplication::allWidgets());
}

//  QWidgetList QApplication::topLevelWidgets()
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN12QApplication15topLevelWidgetsEv() {
  return new QList<QWidget *>(QApplication::topLevelWidgets());
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

//  bool QApplication::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QApplication5eventEP6QEvent(QApplication *self, QEvent *a0) {
  return self->event(a0);
}

//  QApplicationPrivate *QApplication::d_func()
extern "C" Q_DECL_EXPORT
QApplicationPrivate *ritual_ZN12QApplication6d_funcEv(QApplication *self) {
  return self->d_func();
}

//  const QApplicationPrivate *QApplication::d_func() const
extern "C" Q_DECL_EXPORT
const QApplicationPrivate *ritual_ZNK12QApplication6d_funcEv(
    const QApplication *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQApplication, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QApplication(
    QApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQApplication *>(self)->take(key, call);
}

//  bool QApplication::notify(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QApplication6notifyEP7QObjectP6QEvent(
    QApplication *self,
    QObject *a0,
    QEvent *a1) {
  return self->QApplication::notify(a0, a1);
}

//  bool QApplication::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QApplication5eventEP6QEvent(
    QApplication *self,
    QEvent *a0) {
  return static_cast<OwnQApplication *>(self)->OwnQApplication::event(a0);
}
