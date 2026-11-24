//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbutton.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QToolButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQToolButton : QToolButton {
  using QToolButton::event;
  using QToolButton::mousePressEvent;
  using QToolButton::mouseReleaseEvent;
  using QToolButton::paintEvent;
  using QToolButton::actionEvent;
  using QToolButton::enterEvent;
  using QToolButton::leaveEvent;
  using QToolButton::timerEvent;
  using QToolButton::changeEvent;
  using QToolButton::hitButton;
  using QToolButton::checkStateSet;
  using QToolButton::nextCheckState;
  using QToolButton::initStyleOption;
};

//  A QToolButton that Python can take functions over in. Every QToolButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(toolbutton)
typedef const QSize * (*CuteQToolButtonCall0)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
typedef const QSize * (*CuteQToolButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
typedef bool (*CuteQToolButtonCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall5)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall6)(const void *, QActionEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall7)(const void *, QEnterEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall9)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall10)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
typedef bool (*CuteQToolButtonCall11)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall12)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall13)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQToolButtonCall14)(const void *, QStyleOptionToolButton *, int *);
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQToolButtonCall15)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQToolButtonCall16)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQToolButtonCall17)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQToolButtonCall18)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQToolButtonCall19)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
typedef int (*CuteQToolButtonCall20)(const void *, int *);
typedef void (*CuteQToolButtonCall21)(const void *, bool, int *);
typedef int (*CuteQToolButtonCall22)(const void *, int, int *);
typedef bool (*CuteQToolButtonCall23)(const void *, int *);
typedef void * (*CuteQToolButtonCall24)(const void *, int *);
typedef void (*CuteQToolButtonCall25)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQToolButtonCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQToolButtonCall27)(const void *, QMoveEvent *, int *);
typedef void (*CuteQToolButtonCall28)(const void *, QResizeEvent *, int *);
typedef void (*CuteQToolButtonCall29)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQToolButtonCall30)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQToolButtonCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolButtonCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolButtonCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolButtonCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolButtonCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQToolButtonCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQToolButtonCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQToolButtonCall38)(const void *, int, int *);
typedef void (*CuteQToolButtonCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQToolButtonCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQToolButtonCall41)(const void *, int *);
typedef void (*CuteQToolButtonCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQToolButtonCall43)(const void *, int, int *);
typedef bool (*CuteQToolButtonCall44)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQToolButtonCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolButtonCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolButtonCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolButtonCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolButtonCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQToolButton : public QToolButton {
public:
  using QToolButton::QToolButton;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK11QToolButton15initStyleOptionEP22QStyleOptionToolButton")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[29] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
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

#if QT_CONFIG(toolbutton)
  //  QSize QToolButton::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolButtonCall0 call = reinterpret_cast<CuteQToolButtonCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QToolButton::sizeHint();
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
  //  QSize QToolButton::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolButtonCall1 call = reinterpret_cast<CuteQToolButtonCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QToolButton::minimumSizeHint();
  }
#endif  // QT_CONFIG(toolbutton)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
  //  bool QToolButton::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolButtonCall2 call = reinterpret_cast<CuteQToolButtonCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QToolButton::event(e);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolButtonCall3 call = reinterpret_cast<CuteQToolButtonCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolButtonCall4 call = reinterpret_cast<CuteQToolButtonCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolButtonCall5 call = reinterpret_cast<CuteQToolButtonCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::paintEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbutton)
  //  void QToolButton::actionEvent(QActionEvent *a0)
  void actionEvent(QActionEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolButtonCall6 call = reinterpret_cast<CuteQToolButtonCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::actionEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::enterEvent(QEnterEvent *a0)
  void enterEvent(QEnterEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolButtonCall7 call = reinterpret_cast<CuteQToolButtonCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::enterEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolButtonCall8 call = reinterpret_cast<CuteQToolButtonCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::leaveEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbutton)
  //  void QToolButton::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolButtonCall9 call = reinterpret_cast<CuteQToolButtonCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::timerEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolButtonCall10 call = reinterpret_cast<CuteQToolButtonCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolButton::changeEvent(a0);
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
  //  bool QToolButton::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolButtonCall11 call = reinterpret_cast<CuteQToolButtonCall11>(taken[11]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QToolButton::hitButton(pos);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
  //  void QToolButton::checkStateSet()
  void checkStateSet() override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolButtonCall12 call = reinterpret_cast<CuteQToolButtonCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QToolButton::checkStateSet();
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
  //  void QToolButton::nextCheckState()
  void nextCheckState() override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolButtonCall13 call = reinterpret_cast<CuteQToolButtonCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QToolButton::nextCheckState();
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(toolbutton)
  //  void QToolButton::initStyleOption(QStyleOptionToolButton *option)
  //      const
  void initStyleOption(QStyleOptionToolButton *option) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolButtonCall14 call = reinterpret_cast<CuteQToolButtonCall14>(taken[14]);
      call(this, option, &handled);
      if (handled) return;
    }
    QToolButton::initStyleOption(option);
  }
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolButtonCall15 call = reinterpret_cast<CuteQToolButtonCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyPressEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQToolButtonCall16 call = reinterpret_cast<CuteQToolButtonCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQToolButtonCall17 call = reinterpret_cast<CuteQToolButtonCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQToolButtonCall18 call = reinterpret_cast<CuteQToolButtonCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusInEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQToolButtonCall19 call = reinterpret_cast<CuteQToolButtonCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::focusOutEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQToolButtonCall20 call = reinterpret_cast<CuteQToolButtonCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[21]) {
      int handled = 0;
      CuteQToolButtonCall21 call = reinterpret_cast<CuteQToolButtonCall21>(taken[21]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQToolButtonCall22 call = reinterpret_cast<CuteQToolButtonCall22>(taken[22]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQToolButtonCall23 call = reinterpret_cast<CuteQToolButtonCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQToolButtonCall24 call = reinterpret_cast<CuteQToolButtonCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQToolButtonCall25 call = reinterpret_cast<CuteQToolButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQToolButtonCall26 call = reinterpret_cast<CuteQToolButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQToolButtonCall27 call = reinterpret_cast<CuteQToolButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQToolButtonCall28 call = reinterpret_cast<CuteQToolButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQToolButtonCall29 call = reinterpret_cast<CuteQToolButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQToolButtonCall30 call = reinterpret_cast<CuteQToolButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQToolButtonCall31 call = reinterpret_cast<CuteQToolButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQToolButtonCall32 call = reinterpret_cast<CuteQToolButtonCall32>(taken[32]);
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
      CuteQToolButtonCall33 call = reinterpret_cast<CuteQToolButtonCall33>(taken[33]);
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
      CuteQToolButtonCall34 call = reinterpret_cast<CuteQToolButtonCall34>(taken[34]);
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
      CuteQToolButtonCall35 call = reinterpret_cast<CuteQToolButtonCall35>(taken[35]);
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
      CuteQToolButtonCall36 call = reinterpret_cast<CuteQToolButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQToolButtonCall37 call = reinterpret_cast<CuteQToolButtonCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQToolButtonCall38 call = reinterpret_cast<CuteQToolButtonCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQToolButtonCall39 call = reinterpret_cast<CuteQToolButtonCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQToolButtonCall40 call = reinterpret_cast<CuteQToolButtonCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQToolButtonCall41 call = reinterpret_cast<CuteQToolButtonCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQToolButtonCall42 call = reinterpret_cast<CuteQToolButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQToolButtonCall43 call = reinterpret_cast<CuteQToolButtonCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQToolButtonCall44 call = reinterpret_cast<CuteQToolButtonCall44>(taken[44]);
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
      CuteQToolButtonCall45 call = reinterpret_cast<CuteQToolButtonCall45>(taken[45]);
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
      CuteQToolButtonCall46 call = reinterpret_cast<CuteQToolButtonCall46>(taken[46]);
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
      CuteQToolButtonCall47 call = reinterpret_cast<CuteQToolButtonCall47>(taken[47]);
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
      CuteQToolButtonCall48 call = reinterpret_cast<CuteQToolButtonCall48>(taken[48]);
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
      CuteQToolButtonCall49 call = reinterpret_cast<CuteQToolButtonCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QToolButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QToolButton10metaObjectEv(
    const QToolButton *self) {
  return self->metaObject();
}

//  QString QToolButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QToolButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QToolButton::tr(s, c, n));
}

//  QToolButton::QToolButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolButton *ritual_ZN11QToolButtonC1EP7QWidget(QWidget *parent) {
  return new CuteQToolButton(parent);
}

//  QToolButton::~QToolButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButtonD1Ev(QToolButton *self) {
  delete self;
}

//  QSize QToolButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QToolButton8sizeHintEv(const QToolButton *self) {
  return new QSize(self->sizeHint());
}

//  QSize QToolButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QToolButton15minimumSizeHintEv(const QToolButton *self) {
  return new QSize(self->minimumSizeHint());
}

//  Qt::ToolButtonStyle QToolButton::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK11QToolButton15toolButtonStyleEv(
    const QToolButton *self) {
  return self->toolButtonStyle();
}

//  Qt::ArrowType QToolButton::arrowType() const
extern "C" Q_DECL_EXPORT
Qt::ArrowType ritual_ZNK11QToolButton9arrowTypeEv(const QToolButton *self) {
  return self->arrowType();
}

//  void QToolButton::setArrowType(Qt::ArrowType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setArrowTypeEN2Qt9ArrowTypeE(
    QToolButton *self,
    Qt::ArrowType type) {
  self->setArrowType(type);
}

#if QT_CONFIG(menu)
//  void QToolButton::setMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton7setMenuEP5QMenu(QToolButton *self, QMenu *menu) {
  self->setMenu(menu);
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  QMenu *QToolButton::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK11QToolButton4menuEv(const QToolButton *self) {
  return self->menu();
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  void QToolButton::setPopupMode(ToolButtonPopupMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setPopupModeENS_19ToolButtonPopupModeE(
    QToolButton *self,
    QToolButton::ToolButtonPopupMode mode) {
  self->setPopupMode(mode);
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  ToolButtonPopupMode QToolButton::popupMode() const
extern "C" Q_DECL_EXPORT
QToolButton::ToolButtonPopupMode ritual_ZNK11QToolButton9popupModeEv(
    const QToolButton *self) {
  return self->popupMode();
}
#endif  // QT_CONFIG(menu)

//  QAction *QToolButton::defaultAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK11QToolButton13defaultActionEv(const QToolButton *self) {
  return self->defaultAction();
}

//  void QToolButton::setAutoRaise(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton12setAutoRaiseEb(QToolButton *self, bool enable) {
  self->setAutoRaise(enable);
}

//  bool QToolButton::autoRaise() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QToolButton9autoRaiseEv(const QToolButton *self) {
  return self->autoRaise();
}

#if QT_CONFIG(menu)
//  void QToolButton::showMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton8showMenuEv(QToolButton *self) {
  self->showMenu();
}
#endif  // QT_CONFIG(menu)

//  void QToolButton::setToolButtonStyle(Qt::ToolButtonStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QToolButton *self,
    Qt::ToolButtonStyle style) {
  self->setToolButtonStyle(style);
}

//  void QToolButton::setDefaultAction(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton16setDefaultActionEP7QAction(
    QToolButton *self,
    QAction *a0) {
  self->setDefaultAction(a0);
}

//  bool QToolButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QToolButton5eventEP6QEvent(QToolButton *self, QEvent *e) {
  return self->event(e);
}

//  void QToolButton::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton15mousePressEventEP11QMouseEvent(
    QToolButton *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QToolButton::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton17mouseReleaseEventEP11QMouseEvent(
    QToolButton *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QToolButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton10paintEventEP11QPaintEvent(
    QToolButton *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QToolButton::actionEvent(QActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton11actionEventEP12QActionEvent(
    QToolButton *self,
    QActionEvent *a0) {
  self->actionEvent(a0);
}

//  void QToolButton::enterEvent(QEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton10enterEventEP11QEnterEvent(
    QToolButton *self,
    QEnterEvent *a0) {
  self->enterEvent(a0);
}

//  void QToolButton::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton10leaveEventEP6QEvent(
    QToolButton *self,
    QEvent *a0) {
  self->leaveEvent(a0);
}

//  void QToolButton::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton10timerEventEP11QTimerEvent(
    QToolButton *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QToolButton::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton11changeEventEP6QEvent(
    QToolButton *self,
    QEvent *a0) {
  self->changeEvent(a0);
}

//  bool QToolButton::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QToolButton9hitButtonERK6QPoint(
    const QToolButton *self,
    const QPoint *pos) {
  return self->hitButton(*pos);
}

//  void QToolButton::checkStateSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton13checkStateSetEv(QToolButton *self) {
  self->checkStateSet();
}

//  void QToolButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QToolButton14nextCheckStateEv(QToolButton *self) {
  self->nextCheckState();
}

//  void QToolButton::initStyleOption(QStyleOptionToolButton *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QToolButton15initStyleOptionEP22QStyleOptionToolButton(
    const QToolButton *self,
    QStyleOptionToolButton *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQToolButton, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolButton(
    QToolButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolButton *>(self)->take(key, call);
}

//  QSize QToolButton::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QToolButton8sizeHintEv(const QToolButton *self) {
  return new QSize(self->QToolButton::sizeHint());
}

//  QSize QToolButton::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QToolButton15minimumSizeHintEv(
    const QToolButton *self) {
  return new QSize(self->QToolButton::minimumSizeHint());
}

//  bool QToolButton::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QToolButton5eventEP6QEvent(
    QToolButton *self,
    QEvent *e) {
  return static_cast<OwnQToolButton *>(self)->OwnQToolButton::event(e);
}

//  void QToolButton::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton15mousePressEventEP11QMouseEvent(
    QToolButton *self,
    QMouseEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::mousePressEvent(a0);
}

//  void QToolButton::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton17mouseReleaseEventEP11QMouseEvent(
    QToolButton *self,
    QMouseEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::mouseReleaseEvent(a0);
}

//  void QToolButton::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton10paintEventEP11QPaintEvent(
    QToolButton *self,
    QPaintEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::paintEvent(a0);
}

//  void QToolButton::actionEvent(QActionEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton11actionEventEP12QActionEvent(
    QToolButton *self,
    QActionEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::actionEvent(a0);
}

//  void QToolButton::enterEvent(QEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton10enterEventEP11QEnterEvent(
    QToolButton *self,
    QEnterEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::enterEvent(a0);
}

//  void QToolButton::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton10leaveEventEP6QEvent(
    QToolButton *self,
    QEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::leaveEvent(a0);
}

//  void QToolButton::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton10timerEventEP11QTimerEvent(
    QToolButton *self,
    QTimerEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::timerEvent(a0);
}

//  void QToolButton::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton11changeEventEP6QEvent(
    QToolButton *self,
    QEvent *a0) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::changeEvent(a0);
}

//  bool QToolButton::hitButton(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QToolButton9hitButtonERK6QPoint(
    const QToolButton *self,
    const QPoint *pos) {
  return static_cast<const OwnQToolButton *>(self)->OwnQToolButton::hitButton(
      *pos);
}

//  void QToolButton::checkStateSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton13checkStateSetEv(QToolButton *self) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::checkStateSet();
}

//  void QToolButton::nextCheckState()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QToolButton14nextCheckStateEv(QToolButton *self) {
  static_cast<OwnQToolButton *>(self)->OwnQToolButton::nextCheckState();
}

//  void QToolButton::initStyleOption(QStyleOptionToolButton *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QToolButton15initStyleOptionEP22QStyleOptionToolButton(
    const QToolButton *self,
    QStyleOptionToolButton *option) {
  static_cast<const OwnQToolButton *>(self)->OwnQToolButton::initStyleOption(
      option);
}

#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(toolbutton)
