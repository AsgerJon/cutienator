//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
#include <QtWidgets/qabstractspinbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractSpinBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractSpinBox : QAbstractSpinBox {
  using QAbstractSpinBox::resizeEvent;
  using QAbstractSpinBox::keyPressEvent;
  using QAbstractSpinBox::keyReleaseEvent;
  using QAbstractSpinBox::wheelEvent;
  using QAbstractSpinBox::focusInEvent;
  using QAbstractSpinBox::focusOutEvent;
  using QAbstractSpinBox::contextMenuEvent;
  using QAbstractSpinBox::changeEvent;
  using QAbstractSpinBox::closeEvent;
  using QAbstractSpinBox::hideEvent;
  using QAbstractSpinBox::mousePressEvent;
  using QAbstractSpinBox::mouseReleaseEvent;
  using QAbstractSpinBox::mouseMoveEvent;
  using QAbstractSpinBox::timerEvent;
  using QAbstractSpinBox::paintEvent;
  using QAbstractSpinBox::showEvent;
  using QAbstractSpinBox::initStyleOption;
  using QAbstractSpinBox::stepEnabled;
};

//  A QAbstractSpinBox that Python can take functions over in. Every QAbstractSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQAbstractSpinBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQAbstractSpinBoxCall1)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef bool (*CuteQAbstractSpinBoxCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxCall3)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall4)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall5)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall6)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall7)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall9)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall10)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall11)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
typedef void (*CuteQAbstractSpinBoxCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall13)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall14)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall15)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall16)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall17)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall18)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall19)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall20)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall21)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxCall22)(const void *, QStyleOptionSpinBox *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAbstractSpinBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
typedef int (*CuteQAbstractSpinBoxCall24)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxCall25)(const void *, bool, int *);
typedef int (*CuteQAbstractSpinBoxCall26)(const void *, int, int *);
typedef bool (*CuteQAbstractSpinBoxCall27)(const void *, int *);
typedef void * (*CuteQAbstractSpinBoxCall28)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxCall29)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAbstractSpinBoxCall30)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractSpinBoxCall31)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractSpinBoxCall32)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAbstractSpinBoxCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractSpinBoxCall34)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractSpinBoxCall35)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractSpinBoxCall36)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractSpinBoxCall37)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractSpinBoxCall38)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQAbstractSpinBoxCall39)(const void *, int, int *);
typedef void (*CuteQAbstractSpinBoxCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractSpinBoxCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractSpinBoxCall42)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxCall43)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQAbstractSpinBoxCall44)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSpinBoxCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSpinBoxCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSpinBoxCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSpinBoxCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSpinBoxCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractSpinBox : public QAbstractSpinBox {
public:
  using QAbstractSpinBox::QAbstractSpinBox;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox6stepByEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox5clearEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox11stepEnabledEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[32] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
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

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall0 call = reinterpret_cast<CuteQAbstractSpinBoxCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::sizeHint();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall1 call = reinterpret_cast<CuteQAbstractSpinBoxCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::minimumSizeHint();
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
  //  bool QAbstractSpinBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall2 call = reinterpret_cast<CuteQAbstractSpinBoxCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractSpinBox::event(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall3 call = reinterpret_cast<CuteQAbstractSpinBoxCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall4 call = reinterpret_cast<CuteQAbstractSpinBoxCall4>(taken[4]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::stepBy(steps);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::clear()
  void clear() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall5 call = reinterpret_cast<CuteQAbstractSpinBoxCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::clear();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall6 call = reinterpret_cast<CuteQAbstractSpinBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall7 call = reinterpret_cast<CuteQAbstractSpinBoxCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyPressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall8 call = reinterpret_cast<CuteQAbstractSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall9 call = reinterpret_cast<CuteQAbstractSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::wheelEvent(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall10 call = reinterpret_cast<CuteQAbstractSpinBoxCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusInEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall11 call = reinterpret_cast<CuteQAbstractSpinBoxCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusOutEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
  //  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall12 call = reinterpret_cast<CuteQAbstractSpinBoxCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall13 call = reinterpret_cast<CuteQAbstractSpinBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall14 call = reinterpret_cast<CuteQAbstractSpinBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall15 call = reinterpret_cast<CuteQAbstractSpinBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall16 call = reinterpret_cast<CuteQAbstractSpinBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mousePressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall17 call = reinterpret_cast<CuteQAbstractSpinBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall18 call = reinterpret_cast<CuteQAbstractSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall19 call = reinterpret_cast<CuteQAbstractSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::timerEvent(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall20 call = reinterpret_cast<CuteQAbstractSpinBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::paintEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall21 call = reinterpret_cast<CuteQAbstractSpinBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::showEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option)
  //      const
  void initStyleOption(QStyleOptionSpinBox *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall22 call = reinterpret_cast<CuteQAbstractSpinBoxCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::initStyleOption(option);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  StepEnabled QAbstractSpinBox::stepEnabled() const
  QAbstractSpinBox::StepEnabled stepEnabled() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall23 call = reinterpret_cast<CuteQAbstractSpinBoxCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstractSpinBox::StepEnabledFlag>::fromInt(given);
    }
    return QAbstractSpinBox::stepEnabled();
  }
#endif  // QT_CONFIG(spinbox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall24 call = reinterpret_cast<CuteQAbstractSpinBoxCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall25 call = reinterpret_cast<CuteQAbstractSpinBoxCall25>(taken[25]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall26 call = reinterpret_cast<CuteQAbstractSpinBoxCall26>(taken[26]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall27 call = reinterpret_cast<CuteQAbstractSpinBoxCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall28 call = reinterpret_cast<CuteQAbstractSpinBoxCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall29 call = reinterpret_cast<CuteQAbstractSpinBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall30 call = reinterpret_cast<CuteQAbstractSpinBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall31 call = reinterpret_cast<CuteQAbstractSpinBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall32 call = reinterpret_cast<CuteQAbstractSpinBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall33 call = reinterpret_cast<CuteQAbstractSpinBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall34 call = reinterpret_cast<CuteQAbstractSpinBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall35 call = reinterpret_cast<CuteQAbstractSpinBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall36 call = reinterpret_cast<CuteQAbstractSpinBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall37 call = reinterpret_cast<CuteQAbstractSpinBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall38 call = reinterpret_cast<CuteQAbstractSpinBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall39 call = reinterpret_cast<CuteQAbstractSpinBoxCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall40 call = reinterpret_cast<CuteQAbstractSpinBoxCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall41 call = reinterpret_cast<CuteQAbstractSpinBoxCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall42 call = reinterpret_cast<CuteQAbstractSpinBoxCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall43 call = reinterpret_cast<CuteQAbstractSpinBoxCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractSpinBoxCall44 call = reinterpret_cast<CuteQAbstractSpinBoxCall44>(taken[44]);
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
      CuteQAbstractSpinBoxCall45 call = reinterpret_cast<CuteQAbstractSpinBoxCall45>(taken[45]);
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
      CuteQAbstractSpinBoxCall46 call = reinterpret_cast<CuteQAbstractSpinBoxCall46>(taken[46]);
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
      CuteQAbstractSpinBoxCall47 call = reinterpret_cast<CuteQAbstractSpinBoxCall47>(taken[47]);
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
      CuteQAbstractSpinBoxCall48 call = reinterpret_cast<CuteQAbstractSpinBoxCall48>(taken[48]);
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
      CuteQAbstractSpinBoxCall49 call = reinterpret_cast<CuteQAbstractSpinBoxCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAbstractSpinBox10metaObjectEv(
    const QAbstractSpinBox *self) {
  return self->metaObject();
}

//  QString QAbstractSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAbstractSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSpinBox::tr(s, c, n));
}

//  QAbstractSpinBox::QAbstractSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractSpinBox *ritual_ZN16QAbstractSpinBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQAbstractSpinBox(parent);
}

//  QAbstractSpinBox::~QAbstractSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBoxD1Ev(QAbstractSpinBox *self) {
  delete self;
}

//  ButtonSymbols QAbstractSpinBox::buttonSymbols() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::ButtonSymbols ritual_ZNK16QAbstractSpinBox13buttonSymbolsEv(
    const QAbstractSpinBox *self) {
  return self->buttonSymbols();
}

//  void QAbstractSpinBox::setButtonSymbols(ButtonSymbols bs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox16setButtonSymbolsENS_13ButtonSymbolsE(
    QAbstractSpinBox *self,
    QAbstractSpinBox::ButtonSymbols bs) {
  self->setButtonSymbols(bs);
}

//  void QAbstractSpinBox::setCorrectionMode(CorrectionMode cm)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox17setCorrectionModeENS_14CorrectionModeE(
    QAbstractSpinBox *self,
    QAbstractSpinBox::CorrectionMode cm) {
  self->setCorrectionMode(cm);
}

//  CorrectionMode QAbstractSpinBox::correctionMode() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::CorrectionMode ritual_ZNK16QAbstractSpinBox14correctionModeEv(
    const QAbstractSpinBox *self) {
  return self->correctionMode();
}

//  bool QAbstractSpinBox::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox18hasAcceptableInputEv(
    const QAbstractSpinBox *self) {
  return self->hasAcceptableInput();
}

//  QString QAbstractSpinBox::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAbstractSpinBox4textEv(const QAbstractSpinBox *self) {
  return new QString(self->text());
}

//  QString QAbstractSpinBox::specialValueText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QAbstractSpinBox16specialValueTextEv(
    const QAbstractSpinBox *self) {
  return new QString(self->specialValueText());
}

//  void QAbstractSpinBox::setSpecialValueText(const QString &txt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox19setSpecialValueTextERK7QString(
    QAbstractSpinBox *self,
    const QString *txt) {
  self->setSpecialValueText(*txt);
}

//  bool QAbstractSpinBox::wrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox8wrappingEv(const QAbstractSpinBox *self) {
  return self->wrapping();
}

//  void QAbstractSpinBox::setWrapping(bool w)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11setWrappingEb(
    QAbstractSpinBox *self,
    bool w) {
  self->setWrapping(w);
}

//  void QAbstractSpinBox::setReadOnly(bool r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11setReadOnlyEb(
    QAbstractSpinBox *self,
    bool r) {
  self->setReadOnly(r);
}

//  bool QAbstractSpinBox::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox10isReadOnlyEv(
    const QAbstractSpinBox *self) {
  return self->isReadOnly();
}

//  void QAbstractSpinBox::setKeyboardTracking(bool kt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox19setKeyboardTrackingEb(
    QAbstractSpinBox *self,
    bool kt) {
  self->setKeyboardTracking(kt);
}

//  bool QAbstractSpinBox::keyboardTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox16keyboardTrackingEv(
    const QAbstractSpinBox *self) {
  return self->keyboardTracking();
}

//  void QAbstractSpinBox::setAlignment(Qt::Alignment flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractSpinBox *self,
    int flag) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(flag));
}

//  Qt::Alignment QAbstractSpinBox::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstractSpinBox9alignmentEv(const QAbstractSpinBox *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QAbstractSpinBox::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox8setFrameEb(
    QAbstractSpinBox *self,
    bool a0) {
  self->setFrame(a0);
}

//  bool QAbstractSpinBox::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox8hasFrameEv(const QAbstractSpinBox *self) {
  return self->hasFrame();
}

//  void QAbstractSpinBox::setAccelerated(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox14setAcceleratedEb(
    QAbstractSpinBox *self,
    bool on) {
  self->setAccelerated(on);
}

//  bool QAbstractSpinBox::isAccelerated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox13isAcceleratedEv(
    const QAbstractSpinBox *self) {
  return self->isAccelerated();
}

//  void QAbstractSpinBox::setGroupSeparatorShown(bool shown)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox22setGroupSeparatorShownEb(
    QAbstractSpinBox *self,
    bool shown) {
  self->setGroupSeparatorShown(shown);
}

//  bool QAbstractSpinBox::isGroupSeparatorShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAbstractSpinBox21isGroupSeparatorShownEv(
    const QAbstractSpinBox *self) {
  return self->isGroupSeparatorShown();
}

//  QSize QAbstractSpinBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QAbstractSpinBox8sizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->sizeHint());
}

//  QSize QAbstractSpinBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QAbstractSpinBox15minimumSizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QAbstractSpinBox::interpretText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox13interpretTextEv(QAbstractSpinBox *self) {
  self->interpretText();
}

//  bool QAbstractSpinBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QAbstractSpinBox5eventEP6QEvent(
    QAbstractSpinBox *self,
    QEvent *event) {
  return self->event(event);
}

//  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QAbstractSpinBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractSpinBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  void QAbstractSpinBox::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox6stepByEi(
    QAbstractSpinBox *self,
    int steps) {
  self->stepBy(steps);
}

//  void QAbstractSpinBox::stepUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox6stepUpEv(QAbstractSpinBox *self) {
  self->stepUp();
}

//  void QAbstractSpinBox::stepDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox8stepDownEv(QAbstractSpinBox *self) {
  self->stepDown();
}

//  void QAbstractSpinBox::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox9selectAllEv(QAbstractSpinBox *self) {
  self->selectAll();
}

//  void QAbstractSpinBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox5clearEv(QAbstractSpinBox *self) {
  self->clear();
}

//  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11resizeEventEP12QResizeEvent(
    QAbstractSpinBox *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox13keyPressEventEP9QKeyEvent(
    QAbstractSpinBox *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox15keyReleaseEventEP9QKeyEvent(
    QAbstractSpinBox *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

#if QT_CONFIG(wheelevent)
//  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox10wheelEventEP11QWheelEvent(
    QAbstractSpinBox *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox12focusInEventEP11QFocusEvent(
    QAbstractSpinBox *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox13focusOutEventEP11QFocusEvent(
    QAbstractSpinBox *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(contextmenu)
//  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox16contextMenuEventEP17QContextMenuEvent(
    QAbstractSpinBox *self,
    QContextMenuEvent *event) {
  self->contextMenuEvent(event);
}
#endif  // QT_CONFIG(contextmenu)

//  void QAbstractSpinBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11changeEventEP6QEvent(
    QAbstractSpinBox *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox10closeEventEP11QCloseEvent(
    QAbstractSpinBox *self,
    QCloseEvent *event) {
  self->closeEvent(event);
}

//  void QAbstractSpinBox::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox9hideEventEP10QHideEvent(
    QAbstractSpinBox *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox15mousePressEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox17mouseReleaseEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox14mouseMoveEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox10timerEventEP11QTimerEvent(
    QAbstractSpinBox *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox10paintEventEP11QPaintEvent(
    QAbstractSpinBox *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QAbstractSpinBox::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox9showEventEP10QShowEvent(
    QAbstractSpinBox *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox(
    const QAbstractSpinBox *self,
    QStyleOptionSpinBox *option) {
  self->initStyleOption(option);
}

//  QLineEdit *QAbstractSpinBox::lineEdit() const
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZNK16QAbstractSpinBox8lineEditEv(
    const QAbstractSpinBox *self) {
  return self->lineEdit();
}

//  void QAbstractSpinBox::setLineEdit(QLineEdit *edit)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAbstractSpinBox11setLineEditEP9QLineEdit(
    QAbstractSpinBox *self,
    QLineEdit *edit) {
  self->setLineEdit(edit);
}

//  StepEnabled QAbstractSpinBox::stepEnabled() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAbstractSpinBox11stepEnabledEv(
    const QAbstractSpinBox *self) {
  return static_cast<int>(self->stepEnabled().toInt());
}

//  QAbstractSpinBoxPrivate *QAbstractSpinBox::d_func()
extern "C" Q_DECL_EXPORT
QAbstractSpinBoxPrivate *ritual_ZN16QAbstractSpinBox6d_funcEv(
    QAbstractSpinBox *self) {
  return self->d_func();
}

//  const QAbstractSpinBoxPrivate *QAbstractSpinBox::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSpinBoxPrivate *ritual_ZNK16QAbstractSpinBox6d_funcEv(
    const QAbstractSpinBox *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractSpinBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSpinBox(
    QAbstractSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSpinBox *>(self)->take(key, call);
}

//  QSize QAbstractSpinBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK16QAbstractSpinBox8sizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->QAbstractSpinBox::sizeHint());
}

//  QSize QAbstractSpinBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK16QAbstractSpinBox15minimumSizeHintEv(
    const QAbstractSpinBox *self) {
  return new QSize(self->QAbstractSpinBox::minimumSizeHint());
}

//  bool QAbstractSpinBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QAbstractSpinBox5eventEP6QEvent(
    QAbstractSpinBox *self,
    QEvent *event) {
  return self->QAbstractSpinBox::event(event);
}

//  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QAbstractSpinBox16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractSpinBox *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->QAbstractSpinBox::inputMethodQuery(a0));
}

//  void QAbstractSpinBox::stepBy(int steps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox6stepByEi(
    QAbstractSpinBox *self,
    int steps) {
  self->QAbstractSpinBox::stepBy(steps);
}

//  void QAbstractSpinBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox5clearEv(QAbstractSpinBox *self) {
  self->QAbstractSpinBox::clear();
}

//  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox11resizeEventEP12QResizeEvent(
    QAbstractSpinBox *self,
    QResizeEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::resizeEvent(
      event);
}

//  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox13keyPressEventEP9QKeyEvent(
    QAbstractSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::keyPressEvent(
      event);
}

//  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox15keyReleaseEventEP9QKeyEvent(
    QAbstractSpinBox *self,
    QKeyEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::keyReleaseEvent(
      event);
}

#if QT_CONFIG(wheelevent)
//  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox10wheelEventEP11QWheelEvent(
    QAbstractSpinBox *self,
    QWheelEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::wheelEvent(
      event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox12focusInEventEP11QFocusEvent(
    QAbstractSpinBox *self,
    QFocusEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::focusInEvent(
      event);
}

//  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox13focusOutEventEP11QFocusEvent(
    QAbstractSpinBox *self,
    QFocusEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::focusOutEvent(
      event);
}

#if QT_CONFIG(contextmenu)
//  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox16contextMenuEventEP17QContextMenuEvent(
    QAbstractSpinBox *self,
    QContextMenuEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::contextMenuEvent(
      event);
}
#endif  // QT_CONFIG(contextmenu)

//  void QAbstractSpinBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox11changeEventEP6QEvent(
    QAbstractSpinBox *self,
    QEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::changeEvent(
      event);
}

//  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox10closeEventEP11QCloseEvent(
    QAbstractSpinBox *self,
    QCloseEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::closeEvent(
      event);
}

//  void QAbstractSpinBox::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox9hideEventEP10QHideEvent(
    QAbstractSpinBox *self,
    QHideEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::hideEvent(
      event);
}

//  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox15mousePressEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::mousePressEvent(
      event);
}

//  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox17mouseReleaseEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::mouseReleaseEvent(
      event);
}

//  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox14mouseMoveEventEP11QMouseEvent(
    QAbstractSpinBox *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::mouseMoveEvent(
      event);
}

//  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox10timerEventEP11QTimerEvent(
    QAbstractSpinBox *self,
    QTimerEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::timerEvent(
      event);
}

//  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox10paintEventEP11QPaintEvent(
    QAbstractSpinBox *self,
    QPaintEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::paintEvent(
      event);
}

//  void QAbstractSpinBox::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QAbstractSpinBox9showEventEP10QShowEvent(
    QAbstractSpinBox *self,
    QShowEvent *event) {
  static_cast<OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::showEvent(
      event);
}

//  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox(
    const QAbstractSpinBox *self,
    QStyleOptionSpinBox *option) {
  static_cast<const OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::initStyleOption(
      option);
}

//  StepEnabled QAbstractSpinBox::stepEnabled() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QAbstractSpinBox11stepEnabledEv(
    const QAbstractSpinBox *self) {
  return static_cast<int>(
      static_cast<const OwnQAbstractSpinBox *>(self)->OwnQAbstractSpinBox::stepEnabled().toInt());
}

#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(spinbox)
