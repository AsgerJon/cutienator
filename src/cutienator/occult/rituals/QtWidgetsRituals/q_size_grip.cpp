//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsizegrip.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(sizegrip)
#include <QtWidgets/qsizegrip.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSizeGrip may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSizeGrip : QSizeGrip {
  using QSizeGrip::paintEvent;
  using QSizeGrip::mousePressEvent;
  using QSizeGrip::mouseMoveEvent;
  using QSizeGrip::mouseReleaseEvent;
  using QSizeGrip::moveEvent;
  using QSizeGrip::showEvent;
  using QSizeGrip::hideEvent;
  using QSizeGrip::eventFilter;
  using QSizeGrip::event;
};

//  A QSizeGrip that Python can take functions over in. Every QSizeGrip
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(sizegrip)
typedef const QSize * (*CuteQSizeGripCall0)(const void *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall2)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall6)(const void *, QMoveEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall7)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
typedef void (*CuteQSizeGripCall8)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
typedef bool (*CuteQSizeGripCall9)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
typedef bool (*CuteQSizeGripCall10)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQSizeGripCall11)(const void *, int *);
typedef const QSize * (*CuteQSizeGripCall12)(const void *, int *);
typedef int (*CuteQSizeGripCall13)(const void *, int, int *);
typedef bool (*CuteQSizeGripCall14)(const void *, int *);
typedef void * (*CuteQSizeGripCall15)(const void *, int *);
typedef void (*CuteQSizeGripCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQSizeGripCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQSizeGripCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSizeGripCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSizeGripCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSizeGripCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSizeGripCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSizeGripCall23)(const void *, QEvent *, int *);
typedef void (*CuteQSizeGripCall24)(const void *, QResizeEvent *, int *);
typedef void (*CuteQSizeGripCall25)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQSizeGripCall26)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQSizeGripCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQSizeGripCall28)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSizeGripCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSizeGripCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSizeGripCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSizeGripCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQSizeGripCall33)(const void *, QEvent *, int *);
typedef int (*CuteQSizeGripCall34)(const void *, int, int *);
typedef void (*CuteQSizeGripCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQSizeGripCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQSizeGripCall37)(const void *, int *);
typedef void (*CuteQSizeGripCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQSizeGripCall39)(const void *, int, int *);
typedef bool (*CuteQSizeGripCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSizeGripCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSizeGripCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSizeGripCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSizeGripCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSizeGripCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSizeGrip : public QSizeGrip {
public:
  using QSizeGrip::QSizeGrip;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(sizegrip)
  //  QSize QSizeGrip::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSizeGripCall0 call = reinterpret_cast<CuteQSizeGripCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSizeGrip::sizeHint();
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSizeGripCall1 call = reinterpret_cast<CuteQSizeGripCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSizeGrip::setVisible(a0);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSizeGripCall2 call = reinterpret_cast<CuteQSizeGripCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSizeGrip::paintEvent(a0);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSizeGripCall3 call = reinterpret_cast<CuteQSizeGripCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSizeGrip::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSizeGripCall4 call = reinterpret_cast<CuteQSizeGripCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSizeGrip::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::mouseReleaseEvent(QMouseEvent *mouseEvent)
  void mouseReleaseEvent(QMouseEvent *mouseEvent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSizeGripCall5 call = reinterpret_cast<CuteQSizeGripCall5>(taken[5]);
      call(this, mouseEvent, &handled);
      if (handled) return;
    }
    QSizeGrip::mouseReleaseEvent(mouseEvent);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::moveEvent(QMoveEvent *moveEvent)
  void moveEvent(QMoveEvent *moveEvent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSizeGripCall6 call = reinterpret_cast<CuteQSizeGripCall6>(taken[6]);
      call(this, moveEvent, &handled);
      if (handled) return;
    }
    QSizeGrip::moveEvent(moveEvent);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::showEvent(QShowEvent *showEvent)
  void showEvent(QShowEvent *showEvent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSizeGripCall7 call = reinterpret_cast<CuteQSizeGripCall7>(taken[7]);
      call(this, showEvent, &handled);
      if (handled) return;
    }
    QSizeGrip::showEvent(showEvent);
  }
#endif  // QT_CONFIG(sizegrip)

#if QT_CONFIG(sizegrip)
  //  void QSizeGrip::hideEvent(QHideEvent *hideEvent)
  void hideEvent(QHideEvent *hideEvent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSizeGripCall8 call = reinterpret_cast<CuteQSizeGripCall8>(taken[8]);
      call(this, hideEvent, &handled);
      if (handled) return;
    }
    QSizeGrip::hideEvent(hideEvent);
  }
#endif  // QT_CONFIG(sizegrip)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
  //  bool QSizeGrip::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSizeGripCall9 call = reinterpret_cast<CuteQSizeGripCall9>(taken[9]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QSizeGrip::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(sizegrip)
  //  bool QSizeGrip::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSizeGripCall10 call = reinterpret_cast<CuteQSizeGripCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSizeGrip::event(a0);
  }
#endif  // QT_CONFIG(sizegrip)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSizeGripCall11 call = reinterpret_cast<CuteQSizeGripCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSizeGripCall12 call = reinterpret_cast<CuteQSizeGripCall12>(taken[12]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSizeGripCall13 call = reinterpret_cast<CuteQSizeGripCall13>(taken[13]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSizeGripCall14 call = reinterpret_cast<CuteQSizeGripCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSizeGripCall15 call = reinterpret_cast<CuteQSizeGripCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSizeGripCall16 call = reinterpret_cast<CuteQSizeGripCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSizeGripCall17 call = reinterpret_cast<CuteQSizeGripCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSizeGripCall18 call = reinterpret_cast<CuteQSizeGripCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSizeGripCall19 call = reinterpret_cast<CuteQSizeGripCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSizeGripCall20 call = reinterpret_cast<CuteQSizeGripCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSizeGripCall21 call = reinterpret_cast<CuteQSizeGripCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSizeGripCall22 call = reinterpret_cast<CuteQSizeGripCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSizeGripCall23 call = reinterpret_cast<CuteQSizeGripCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSizeGripCall24 call = reinterpret_cast<CuteQSizeGripCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSizeGripCall25 call = reinterpret_cast<CuteQSizeGripCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSizeGripCall26 call = reinterpret_cast<CuteQSizeGripCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSizeGripCall27 call = reinterpret_cast<CuteQSizeGripCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSizeGripCall28 call = reinterpret_cast<CuteQSizeGripCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSizeGripCall29 call = reinterpret_cast<CuteQSizeGripCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSizeGripCall30 call = reinterpret_cast<CuteQSizeGripCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSizeGripCall31 call = reinterpret_cast<CuteQSizeGripCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSizeGripCall32 call = reinterpret_cast<CuteQSizeGripCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSizeGripCall33 call = reinterpret_cast<CuteQSizeGripCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQSizeGripCall34 call = reinterpret_cast<CuteQSizeGripCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQSizeGripCall35 call = reinterpret_cast<CuteQSizeGripCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSizeGripCall36 call = reinterpret_cast<CuteQSizeGripCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQSizeGripCall37 call = reinterpret_cast<CuteQSizeGripCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQSizeGripCall38 call = reinterpret_cast<CuteQSizeGripCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQSizeGripCall39 call = reinterpret_cast<CuteQSizeGripCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSizeGripCall40 call = reinterpret_cast<CuteQSizeGripCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQSizeGripCall41 call = reinterpret_cast<CuteQSizeGripCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQSizeGripCall42 call = reinterpret_cast<CuteQSizeGripCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQSizeGripCall43 call = reinterpret_cast<CuteQSizeGripCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQSizeGripCall44 call = reinterpret_cast<CuteQSizeGripCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQSizeGripCall45 call = reinterpret_cast<CuteQSizeGripCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSizeGrip::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSizeGrip10metaObjectEv(
    const QSizeGrip *self) {
  return self->metaObject();
}

//  QString QSizeGrip::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSizeGrip2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSizeGrip::tr(s, c, n));
}

//  QSizeGrip::QSizeGrip(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSizeGrip *ritual_ZN9QSizeGripC1EP7QWidget(QWidget *parent) {
  return new CuteQSizeGrip(parent);
}

//  QSizeGrip::~QSizeGrip()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGripD1Ev(QSizeGrip *self) {
  delete self;
}

//  QSize QSizeGrip::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSizeGrip8sizeHintEv(const QSizeGrip *self) {
  return new QSize(self->sizeHint());
}

//  void QSizeGrip::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip10setVisibleEb(QSizeGrip *self, bool a0) {
  self->setVisible(a0);
}

//  void QSizeGrip::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip10paintEventEP11QPaintEvent(
    QSizeGrip *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QSizeGrip::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip15mousePressEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QSizeGrip::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip14mouseMoveEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QSizeGrip::mouseReleaseEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip17mouseReleaseEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *mouseEvent) {
  self->mouseReleaseEvent(mouseEvent);
}

//  void QSizeGrip::moveEvent(QMoveEvent *moveEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip9moveEventEP10QMoveEvent(
    QSizeGrip *self,
    QMoveEvent *moveEvent) {
  self->moveEvent(moveEvent);
}

//  void QSizeGrip::showEvent(QShowEvent *showEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip9showEventEP10QShowEvent(
    QSizeGrip *self,
    QShowEvent *showEvent) {
  self->showEvent(showEvent);
}

//  void QSizeGrip::hideEvent(QHideEvent *hideEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip9hideEventEP10QHideEvent(
    QSizeGrip *self,
    QHideEvent *hideEvent) {
  self->hideEvent(hideEvent);
}

//  bool QSizeGrip::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSizeGrip11eventFilterEP7QObjectP6QEvent(
    QSizeGrip *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  bool QSizeGrip::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSizeGrip5eventEP6QEvent(QSizeGrip *self, QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQSizeGrip, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSizeGrip(QSizeGrip *self, const char *key, void *call) {
  return static_cast<CuteQSizeGrip *>(self)->take(key, call);
}

//  QSize QSizeGrip::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QSizeGrip8sizeHintEv(const QSizeGrip *self) {
  return new QSize(self->QSizeGrip::sizeHint());
}

//  void QSizeGrip::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip10setVisibleEb(QSizeGrip *self, bool a0) {
  self->QSizeGrip::setVisible(a0);
}

//  void QSizeGrip::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip10paintEventEP11QPaintEvent(
    QSizeGrip *self,
    QPaintEvent *a0) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::paintEvent(a0);
}

//  void QSizeGrip::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip15mousePressEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *a0) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::mousePressEvent(a0);
}

//  void QSizeGrip::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip14mouseMoveEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *a0) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::mouseMoveEvent(a0);
}

//  void QSizeGrip::mouseReleaseEvent(QMouseEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip17mouseReleaseEventEP11QMouseEvent(
    QSizeGrip *self,
    QMouseEvent *mouseEvent) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::mouseReleaseEvent(
      mouseEvent);
}

//  void QSizeGrip::moveEvent(QMoveEvent *moveEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip9moveEventEP10QMoveEvent(
    QSizeGrip *self,
    QMoveEvent *moveEvent) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::moveEvent(moveEvent);
}

//  void QSizeGrip::showEvent(QShowEvent *showEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip9showEventEP10QShowEvent(
    QSizeGrip *self,
    QShowEvent *showEvent) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::showEvent(showEvent);
}

//  void QSizeGrip::hideEvent(QHideEvent *hideEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSizeGrip9hideEventEP10QHideEvent(
    QSizeGrip *self,
    QHideEvent *hideEvent) {
  static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::hideEvent(hideEvent);
}

//  bool QSizeGrip::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QSizeGrip11eventFilterEP7QObjectP6QEvent(
    QSizeGrip *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::eventFilter(
      a0,
      a1);
}

//  bool QSizeGrip::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QSizeGrip5eventEP6QEvent(QSizeGrip *self, QEvent *a0) {
  return static_cast<OwnQSizeGrip *>(self)->OwnQSizeGrip::event(a0);
}

#endif  // QT_CONFIG(sizegrip)
