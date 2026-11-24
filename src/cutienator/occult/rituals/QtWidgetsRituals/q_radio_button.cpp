//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qradiobutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
#include <QtWidgets/qradiobutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRadioButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRadioButton : QRadioButton {
  using QRadioButton::event;
  using QRadioButton::hitButton;
  using QRadioButton::paintEvent;
  using QRadioButton::mouseMoveEvent;
  using QRadioButton::initStyleOption;
};

//  A QRadioButton that Python can take functions over in. Every QRadioButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(radiobutton)
typedef const QSize * (*CuteQRadioButtonCall0)(const void *, int *);
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
typedef const QSize * (*CuteQRadioButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(radiobutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(radiobutton)
typedef bool (*CuteQRadioButtonCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(radiobutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(radiobutton)
typedef bool (*CuteQRadioButtonCall3)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(radiobutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(radiobutton)
typedef void (*CuteQRadioButtonCall4)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
typedef void (*CuteQRadioButtonCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
typedef void (*CuteQRadioButtonCall6)(const void *, QStyleOptionButton *, int *);
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall7)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall8)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall9)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall12)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall13)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall14)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQRadioButtonCall16)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQRadioButtonCall17)(const void *, int *);
typedef void (*CuteQRadioButtonCall18)(const void *, bool, int *);
typedef int (*CuteQRadioButtonCall19)(const void *, int, int *);
typedef bool (*CuteQRadioButtonCall20)(const void *, int *);
typedef void * (*CuteQRadioButtonCall21)(const void *, int *);
typedef void (*CuteQRadioButtonCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQRadioButtonCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQRadioButtonCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQRadioButtonCall25)(const void *, QEvent *, int *);
typedef void (*CuteQRadioButtonCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQRadioButtonCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQRadioButtonCall28)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQRadioButtonCall29)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQRadioButtonCall30)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQRadioButtonCall31)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRadioButtonCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRadioButtonCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRadioButtonCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQRadioButtonCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQRadioButtonCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQRadioButtonCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQRadioButtonCall38)(const void *, int, int *);
typedef void (*CuteQRadioButtonCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQRadioButtonCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQRadioButtonCall41)(const void *, int *);
typedef void (*CuteQRadioButtonCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQRadioButtonCall43)(const void *, int, int *);
typedef bool (*CuteQRadioButtonCall44)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRadioButtonCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRadioButtonCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRadioButtonCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRadioButtonCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRadioButtonCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRadioButton : public QRadioButton {
public:
  using QRadioButton::QRadioButton;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(radiobutton)
    if (!std::strcmp(key, "_ZNK12QRadioButton15initStyleOptionEP18QStyleOptionButton")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(radiobutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[28] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[44] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(radiobutton)
  //  QSize QRadioButton::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRadioButtonCall0 call = reinterpret_cast<CuteQRadioButtonCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRadioButton::sizeHint();
  }
#endif  // QT_CONFIG(radiobutton)

#if QT_CONFIG(radiobutton)
  //  QSize QRadioButton::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRadioButtonCall1 call = reinterpret_cast<CuteQRadioButtonCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRadioButton::minimumSizeHint();
  }
#endif  // QT_CONFIG(radiobutton)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(radiobutton)
  //  bool QRadioButton::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRadioButtonCall2 call = reinterpret_cast<CuteQRadioButtonCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QRadioButton::event(e);
  }
#endif  // QT_CONFIG(radiobutton)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(radiobutton)
  //  bool QRadioButton::hitButton(const QPoint &a0) const
  bool hitButton(const QPoint &a0) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRadioButtonCall3 call = reinterpret_cast<CuteQRadioButtonCall3>(taken[3]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QRadioButton::hitButton(a0);
  }
#endif  // QT_CONFIG(radiobutton)
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(radiobutton)
  //  void QRadioButton::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRadioButtonCall4 call = reinterpret_cast<CuteQRadioButtonCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRadioButton::paintEvent(a0);
  }
#endif  // QT_CONFIG(radiobutton)

#if QT_CONFIG(radiobutton)
  //  void QRadioButton::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRadioButtonCall5 call = reinterpret_cast<CuteQRadioButtonCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRadioButton::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(radiobutton)

#if QT_CONFIG(radiobutton)
  //  void QRadioButton::initStyleOption(QStyleOptionButton *button) const
  void initStyleOption(QStyleOptionButton *button) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRadioButtonCall6 call = reinterpret_cast<CuteQRadioButtonCall6>(taken[6]);
      call(this, button, &handled);
      if (handled) return;
    }
    QRadioButton::initStyleOption(button);
  }
#endif  // QT_CONFIG(radiobutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::checkStateSet()
  void checkStateSet() override {
    if (taken[7]) {
      int handled = 0;
      CuteQRadioButtonCall7 call = reinterpret_cast<CuteQRadioButtonCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::checkStateSet();
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[8]) {
      int handled = 0;
      CuteQRadioButtonCall8 call = reinterpret_cast<CuteQRadioButtonCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::nextCheckState();
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRadioButtonCall9 call = reinterpret_cast<CuteQRadioButtonCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyPressEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQRadioButtonCall10 call = reinterpret_cast<CuteQRadioButtonCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQRadioButtonCall11 call = reinterpret_cast<CuteQRadioButtonCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRadioButtonCall12 call = reinterpret_cast<CuteQRadioButtonCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRadioButtonCall13 call = reinterpret_cast<CuteQRadioButtonCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusInEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRadioButtonCall14 call = reinterpret_cast<CuteQRadioButtonCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusOutEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRadioButtonCall15 call = reinterpret_cast<CuteQRadioButtonCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRadioButtonCall16 call = reinterpret_cast<CuteQRadioButtonCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQRadioButtonCall17 call = reinterpret_cast<CuteQRadioButtonCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRadioButtonCall18 call = reinterpret_cast<CuteQRadioButtonCall18>(taken[18]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQRadioButtonCall19 call = reinterpret_cast<CuteQRadioButtonCall19>(taken[19]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQRadioButtonCall20 call = reinterpret_cast<CuteQRadioButtonCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQRadioButtonCall21 call = reinterpret_cast<CuteQRadioButtonCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRadioButtonCall22 call = reinterpret_cast<CuteQRadioButtonCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRadioButtonCall23 call = reinterpret_cast<CuteQRadioButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRadioButtonCall24 call = reinterpret_cast<CuteQRadioButtonCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRadioButtonCall25 call = reinterpret_cast<CuteQRadioButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRadioButtonCall26 call = reinterpret_cast<CuteQRadioButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRadioButtonCall27 call = reinterpret_cast<CuteQRadioButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRadioButtonCall28 call = reinterpret_cast<CuteQRadioButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRadioButtonCall29 call = reinterpret_cast<CuteQRadioButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRadioButtonCall30 call = reinterpret_cast<CuteQRadioButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRadioButtonCall31 call = reinterpret_cast<CuteQRadioButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRadioButtonCall32 call = reinterpret_cast<CuteQRadioButtonCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRadioButtonCall33 call = reinterpret_cast<CuteQRadioButtonCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRadioButtonCall34 call = reinterpret_cast<CuteQRadioButtonCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRadioButtonCall35 call = reinterpret_cast<CuteQRadioButtonCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRadioButtonCall36 call = reinterpret_cast<CuteQRadioButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRadioButtonCall37 call = reinterpret_cast<CuteQRadioButtonCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQRadioButtonCall38 call = reinterpret_cast<CuteQRadioButtonCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQRadioButtonCall39 call = reinterpret_cast<CuteQRadioButtonCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQRadioButtonCall40 call = reinterpret_cast<CuteQRadioButtonCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRadioButtonCall41 call = reinterpret_cast<CuteQRadioButtonCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQRadioButtonCall42 call = reinterpret_cast<CuteQRadioButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRadioButtonCall43 call = reinterpret_cast<CuteQRadioButtonCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQRadioButtonCall44 call = reinterpret_cast<CuteQRadioButtonCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQRadioButtonCall45 call = reinterpret_cast<CuteQRadioButtonCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQRadioButtonCall46 call = reinterpret_cast<CuteQRadioButtonCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQRadioButtonCall47 call = reinterpret_cast<CuteQRadioButtonCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQRadioButtonCall48 call = reinterpret_cast<CuteQRadioButtonCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQRadioButtonCall49 call = reinterpret_cast<CuteQRadioButtonCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRadioButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QRadioButton10metaObjectEv(
    const QRadioButton *self) {
  return self->metaObject();
}

//  QString QRadioButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QRadioButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRadioButton::tr(s, c, n));
}

//  QRadioButton::QRadioButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QRadioButton *ritual_ZN12QRadioButtonC1EP7QWidget(QWidget *parent) {
  return new CuteQRadioButton(parent);
}

//  QRadioButton::QRadioButton(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QRadioButton *ritual_ZN12QRadioButtonC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQRadioButton(*text, parent);
}

//  QRadioButton::~QRadioButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRadioButtonD1Ev(QRadioButton *self) {
  delete self;
}

//  QSize QRadioButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QRadioButton8sizeHintEv(const QRadioButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QRadioButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QRadioButton15minimumSizeHintEv(
    const QRadioButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  bool QRadioButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QRadioButton5eventEP6QEvent(QRadioButton *self, QEvent *e) {
  return self->event(e);
}

//  bool QRadioButton::hitButton(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QRadioButton9hitButtonERK6QPoint(
    const QRadioButton *self,
    const QPoint *a0) {
  return self->hitButton(*a0);
}

//  void QRadioButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRadioButton10paintEventEP11QPaintEvent(
    QRadioButton *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QRadioButton::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRadioButton14mouseMoveEventEP11QMouseEvent(
    QRadioButton *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QRadioButton::initStyleOption(QStyleOptionButton *button) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QRadioButton15initStyleOptionEP18QStyleOptionButton(
    const QRadioButton *self,
    QStyleOptionButton *button) {
  self->initStyleOption(button);
}

//  a Python function taken by a CuteQRadioButton, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRadioButton(
    QRadioButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRadioButton *>(self)->take(key, call);
}

//  QSize QRadioButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QRadioButton8sizeHintEv(const QRadioButton *self) {
  return new QSize(self->QRadioButton::sizeHint());
}

//  QSize QRadioButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QRadioButton15minimumSizeHintEv(
    const QRadioButton *self) {
  return new QSize(self->QRadioButton::minimumSizeHint());
}

//  bool QRadioButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QRadioButton5eventEP6QEvent(
    QRadioButton *self,
    QEvent *e) {
  return static_cast<OwnQRadioButton *>(self)->OwnQRadioButton::event(e);
}

//  bool QRadioButton::hitButton(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QRadioButton9hitButtonERK6QPoint(
    const QRadioButton *self,
    const QPoint *a0) {
  return static_cast<const OwnQRadioButton *>(self)->OwnQRadioButton::hitButton(
      *a0);
}

//  void QRadioButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QRadioButton10paintEventEP11QPaintEvent(
    QRadioButton *self,
    QPaintEvent *a0) {
  static_cast<OwnQRadioButton *>(self)->OwnQRadioButton::paintEvent(a0);
}

//  void QRadioButton::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QRadioButton14mouseMoveEventEP11QMouseEvent(
    QRadioButton *self,
    QMouseEvent *a0) {
  static_cast<OwnQRadioButton *>(self)->OwnQRadioButton::mouseMoveEvent(a0);
}

//  void QRadioButton::initStyleOption(QStyleOptionButton *button) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK12QRadioButton15initStyleOptionEP18QStyleOptionButton(
    const QRadioButton *self,
    QStyleOptionButton *button) {
  static_cast<const OwnQRadioButton *>(self)->OwnQRadioButton::initStyleOption(
      button);
}

#endif  // QT_CONFIG(radiobutton)
#endif  // QT_CONFIG(radiobutton)
