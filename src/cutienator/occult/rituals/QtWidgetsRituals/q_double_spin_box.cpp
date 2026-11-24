//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qspinbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDoubleSpinBox that Python can take functions over in. Every QDoubleSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(spinbox)
typedef double (*CuteQDoubleSpinBoxCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQDoubleSpinBoxCall1)(const void *, double, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQDoubleSpinBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQDoubleSpinBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef bool (*CuteQDoubleSpinBoxCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDoubleSpinBoxCall5)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall6)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall8)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall9)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall11)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall12)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall13)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
typedef void (*CuteQDoubleSpinBoxCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall16)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall17)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall18)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall19)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall20)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall21)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall22)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall23)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDoubleSpinBoxCall24)(const void *, QStyleOptionSpinBox *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef int (*CuteQDoubleSpinBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
typedef int (*CuteQDoubleSpinBoxCall26)(const void *, int *);
typedef void (*CuteQDoubleSpinBoxCall27)(const void *, bool, int *);
typedef int (*CuteQDoubleSpinBoxCall28)(const void *, int, int *);
typedef bool (*CuteQDoubleSpinBoxCall29)(const void *, int *);
typedef void * (*CuteQDoubleSpinBoxCall30)(const void *, int *);
typedef void (*CuteQDoubleSpinBoxCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDoubleSpinBoxCall32)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDoubleSpinBoxCall33)(const void *, QEvent *, int *);
typedef void (*CuteQDoubleSpinBoxCall34)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDoubleSpinBoxCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDoubleSpinBoxCall36)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDoubleSpinBoxCall37)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDoubleSpinBoxCall38)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDoubleSpinBoxCall39)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDoubleSpinBoxCall40)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQDoubleSpinBoxCall41)(const void *, int, int *);
typedef void (*CuteQDoubleSpinBoxCall42)(const void *, QPainter *, int *);
typedef void * (*CuteQDoubleSpinBoxCall43)(const void *, QPoint *, int *);
typedef void * (*CuteQDoubleSpinBoxCall44)(const void *, int *);
typedef void (*CuteQDoubleSpinBoxCall45)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQDoubleSpinBoxCall46)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDoubleSpinBoxCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleSpinBoxCall48)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleSpinBoxCall49)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleSpinBoxCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDoubleSpinBoxCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDoubleSpinBox : public QDoubleSpinBox {
public:
  using QDoubleSpinBox::QDoubleSpinBox;
  void *taken[52] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK14QDoubleSpinBox13valueFromTextERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK14QDoubleSpinBox13textFromValueEd")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox6stepByEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox5clearEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox11stepEnabledEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(spinbox)
  //  double QDoubleSpinBox::valueFromText(const QString &text) const
  double valueFromText(const QString &text) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall0 call = reinterpret_cast<CuteQDoubleSpinBoxCall0>(taken[0]);
      double given = call(this, &text, &handled);
      if (handled) return given;
    }
    return QDoubleSpinBox::valueFromText(text);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QString QDoubleSpinBox::textFromValue(double val) const
  QString textFromValue(double val) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall1 call = reinterpret_cast<CuteQDoubleSpinBoxCall1>(taken[1]);
      QString * given = call(this, val, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDoubleSpinBox::textFromValue(val);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall2 call = reinterpret_cast<CuteQDoubleSpinBoxCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::sizeHint();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall3 call = reinterpret_cast<CuteQDoubleSpinBoxCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall4 call = reinterpret_cast<CuteQDoubleSpinBoxCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall5 call = reinterpret_cast<CuteQDoubleSpinBoxCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall6 call = reinterpret_cast<CuteQDoubleSpinBoxCall6>(taken[6]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::stepBy(steps);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::clear()
  void clear() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall7 call = reinterpret_cast<CuteQDoubleSpinBoxCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::clear();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall8 call = reinterpret_cast<CuteQDoubleSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall9 call = reinterpret_cast<CuteQDoubleSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyPressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall10 call = reinterpret_cast<CuteQDoubleSpinBoxCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall11 call = reinterpret_cast<CuteQDoubleSpinBoxCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall12 call = reinterpret_cast<CuteQDoubleSpinBoxCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusInEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall13 call = reinterpret_cast<CuteQDoubleSpinBoxCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall14 call = reinterpret_cast<CuteQDoubleSpinBoxCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall15 call = reinterpret_cast<CuteQDoubleSpinBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall16 call = reinterpret_cast<CuteQDoubleSpinBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall17 call = reinterpret_cast<CuteQDoubleSpinBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall18 call = reinterpret_cast<CuteQDoubleSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mousePressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall19 call = reinterpret_cast<CuteQDoubleSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall20 call = reinterpret_cast<CuteQDoubleSpinBoxCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall21 call = reinterpret_cast<CuteQDoubleSpinBoxCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall22 call = reinterpret_cast<CuteQDoubleSpinBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::paintEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall23 call = reinterpret_cast<CuteQDoubleSpinBoxCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall24 call = reinterpret_cast<CuteQDoubleSpinBoxCall24>(taken[24]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::initStyleOption(option);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  StepEnabled QAbstractSpinBox::stepEnabled() const
  QAbstractSpinBox::StepEnabled stepEnabled() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall25 call = reinterpret_cast<CuteQDoubleSpinBoxCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstractSpinBox::StepEnabledFlag>::fromInt(given);
    }
    return QAbstractSpinBox::stepEnabled();
  }
#endif  // QT_CONFIG(spinbox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall26 call = reinterpret_cast<CuteQDoubleSpinBoxCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall27 call = reinterpret_cast<CuteQDoubleSpinBoxCall27>(taken[27]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall28 call = reinterpret_cast<CuteQDoubleSpinBoxCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall29 call = reinterpret_cast<CuteQDoubleSpinBoxCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall30 call = reinterpret_cast<CuteQDoubleSpinBoxCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall31 call = reinterpret_cast<CuteQDoubleSpinBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall32 call = reinterpret_cast<CuteQDoubleSpinBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall33 call = reinterpret_cast<CuteQDoubleSpinBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall34 call = reinterpret_cast<CuteQDoubleSpinBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall35 call = reinterpret_cast<CuteQDoubleSpinBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall36 call = reinterpret_cast<CuteQDoubleSpinBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall37 call = reinterpret_cast<CuteQDoubleSpinBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall38 call = reinterpret_cast<CuteQDoubleSpinBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall39 call = reinterpret_cast<CuteQDoubleSpinBoxCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall40 call = reinterpret_cast<CuteQDoubleSpinBoxCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall41 call = reinterpret_cast<CuteQDoubleSpinBoxCall41>(taken[41]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall42 call = reinterpret_cast<CuteQDoubleSpinBoxCall42>(taken[42]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall43 call = reinterpret_cast<CuteQDoubleSpinBoxCall43>(taken[43]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall44 call = reinterpret_cast<CuteQDoubleSpinBoxCall44>(taken[44]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall45 call = reinterpret_cast<CuteQDoubleSpinBoxCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall46 call = reinterpret_cast<CuteQDoubleSpinBoxCall46>(taken[46]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall47 call = reinterpret_cast<CuteQDoubleSpinBoxCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall48 call = reinterpret_cast<CuteQDoubleSpinBoxCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall49 call = reinterpret_cast<CuteQDoubleSpinBoxCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall50 call = reinterpret_cast<CuteQDoubleSpinBoxCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQDoubleSpinBoxCall51 call = reinterpret_cast<CuteQDoubleSpinBoxCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDoubleSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QDoubleSpinBox10metaObjectEv(
    const QDoubleSpinBox *self) {
  return self->metaObject();
}

//  QString QDoubleSpinBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QDoubleSpinBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDoubleSpinBox::tr(s, c, n));
}

//  QDoubleSpinBox::QDoubleSpinBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDoubleSpinBox *ritual_ZN14QDoubleSpinBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQDoubleSpinBox(parent);
}

//  QDoubleSpinBox::~QDoubleSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBoxD1Ev(QDoubleSpinBox *self) {
  delete self;
}

//  double QDoubleSpinBox::value() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox5valueEv(const QDoubleSpinBox *self) {
  return self->value();
}

//  QString QDoubleSpinBox::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox6prefixEv(const QDoubleSpinBox *self) {
  return new QString(self->prefix());
}

//  void QDoubleSpinBox::setPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox9setPrefixERK7QString(
    QDoubleSpinBox *self,
    const QString *prefix) {
  self->setPrefix(*prefix);
}

//  QString QDoubleSpinBox::suffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox6suffixEv(const QDoubleSpinBox *self) {
  return new QString(self->suffix());
}

//  void QDoubleSpinBox::setSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox9setSuffixERK7QString(
    QDoubleSpinBox *self,
    const QString *suffix) {
  self->setSuffix(*suffix);
}

//  QString QDoubleSpinBox::cleanText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox9cleanTextEv(const QDoubleSpinBox *self) {
  return new QString(self->cleanText());
}

//  double QDoubleSpinBox::singleStep() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox10singleStepEv(const QDoubleSpinBox *self) {
  return self->singleStep();
}

//  void QDoubleSpinBox::setSingleStep(double val)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox13setSingleStepEd(
    QDoubleSpinBox *self,
    double val) {
  self->setSingleStep(val);
}

//  double QDoubleSpinBox::minimum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox7minimumEv(const QDoubleSpinBox *self) {
  return self->minimum();
}

//  void QDoubleSpinBox::setMinimum(double min)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox10setMinimumEd(
    QDoubleSpinBox *self,
    double min) {
  self->setMinimum(min);
}

//  double QDoubleSpinBox::maximum() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox7maximumEv(const QDoubleSpinBox *self) {
  return self->maximum();
}

//  void QDoubleSpinBox::setMaximum(double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox10setMaximumEd(
    QDoubleSpinBox *self,
    double max) {
  self->setMaximum(max);
}

//  void QDoubleSpinBox::setRange(double min, double max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox8setRangeEdd(
    QDoubleSpinBox *self,
    double min,
    double max) {
  self->setRange(min, max);
}

//  StepType QDoubleSpinBox::stepType() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox::StepType ritual_ZNK14QDoubleSpinBox8stepTypeEv(
    const QDoubleSpinBox *self) {
  return self->stepType();
}

//  void QDoubleSpinBox::setStepType(StepType stepType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox11setStepTypeEN16QAbstractSpinBox8StepTypeE(
    QDoubleSpinBox *self,
    QAbstractSpinBox::StepType stepType) {
  self->setStepType(stepType);
}

//  int QDoubleSpinBox::decimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QDoubleSpinBox8decimalsEv(const QDoubleSpinBox *self) {
  return self->decimals();
}

//  void QDoubleSpinBox::setDecimals(int prec)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox11setDecimalsEi(
    QDoubleSpinBox *self,
    int prec) {
  self->setDecimals(prec);
}

//  double QDoubleSpinBox::valueFromText(const QString &text) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QDoubleSpinBox13valueFromTextERK7QString(
    const QDoubleSpinBox *self,
    const QString *text) {
  return self->valueFromText(*text);
}

//  QString QDoubleSpinBox::textFromValue(double val) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDoubleSpinBox13textFromValueEd(
    const QDoubleSpinBox *self,
    double val) {
  return new QString(self->textFromValue(val));
}

//  void QDoubleSpinBox::setValue(double val)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDoubleSpinBox8setValueEd(QDoubleSpinBox *self, double val) {
  self->setValue(val);
}

//  a Python function taken by a CuteQDoubleSpinBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDoubleSpinBox(
    QDoubleSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDoubleSpinBox *>(self)->take(key, call);
}

//  double QDoubleSpinBox::valueFromText(const QString &text) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK14QDoubleSpinBox13valueFromTextERK7QString(
    const QDoubleSpinBox *self,
    const QString *text) {
  return self->QDoubleSpinBox::valueFromText(*text);
}

//  QString QDoubleSpinBox::textFromValue(double val) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QDoubleSpinBox13textFromValueEd(
    const QDoubleSpinBox *self,
    double val) {
  return new QString(self->QDoubleSpinBox::textFromValue(val));
}

#endif  // QT_CONFIG(spinbox)
