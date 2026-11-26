//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsplitter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
#include <QtWidgets/qsplitter.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSplitterHandle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSplitterHandle : QSplitterHandle {
  using QSplitterHandle::paintEvent;
  using QSplitterHandle::mouseMoveEvent;
  using QSplitterHandle::mousePressEvent;
  using QSplitterHandle::mouseReleaseEvent;
  using QSplitterHandle::resizeEvent;
  using QSplitterHandle::event;
};

//  A QSplitterHandle that Python can take functions over in. Every QSplitterHandle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(splitter)
typedef const QSize * (*CuteQSplitterHandleCall0)(const void *, int *);
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
typedef void (*CuteQSplitterHandleCall1)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
typedef void (*CuteQSplitterHandleCall2)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
typedef void (*CuteQSplitterHandleCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
typedef void (*CuteQSplitterHandleCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
typedef void (*CuteQSplitterHandleCall5)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(splitter)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(splitter)
typedef bool (*CuteQSplitterHandleCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(splitter)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQSplitterHandleCall7)(const void *, int *);
typedef void (*CuteQSplitterHandleCall8)(const void *, bool, int *);
typedef const QSize * (*CuteQSplitterHandleCall9)(const void *, int *);
typedef int (*CuteQSplitterHandleCall10)(const void *, int, int *);
typedef bool (*CuteQSplitterHandleCall11)(const void *, int *);
typedef void * (*CuteQSplitterHandleCall12)(const void *, int *);
typedef void (*CuteQSplitterHandleCall13)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQSplitterHandleCall14)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQSplitterHandleCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSplitterHandleCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQSplitterHandleCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSplitterHandleCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQSplitterHandleCall19)(const void *, QEnterEvent *, int *);
typedef void (*CuteQSplitterHandleCall20)(const void *, QEvent *, int *);
typedef void (*CuteQSplitterHandleCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQSplitterHandleCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQSplitterHandleCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQSplitterHandleCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQSplitterHandleCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSplitterHandleCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSplitterHandleCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSplitterHandleCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSplitterHandleCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQSplitterHandleCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQSplitterHandleCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQSplitterHandleCall32)(const void *, QEvent *, int *);
typedef int (*CuteQSplitterHandleCall33)(const void *, int, int *);
typedef void (*CuteQSplitterHandleCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQSplitterHandleCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQSplitterHandleCall36)(const void *, int *);
typedef void (*CuteQSplitterHandleCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQSplitterHandleCall38)(const void *, int, int *);
typedef bool (*CuteQSplitterHandleCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplitterHandleCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplitterHandleCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplitterHandleCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplitterHandleCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplitterHandleCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplitterHandleCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSplitterHandle : public QSplitterHandle {
public:
  using QSplitterHandle::QSplitterHandle;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(splitter)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(splitter)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

#if QT_CONFIG(splitter)
  //  QSize QSplitterHandle::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSplitterHandleCall0 call = reinterpret_cast<CuteQSplitterHandleCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSplitterHandle::sizeHint();
  }
#endif  // QT_CONFIG(splitter)

#if QT_CONFIG(splitter)
  //  void QSplitterHandle::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplitterHandleCall1 call = reinterpret_cast<CuteQSplitterHandleCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitterHandle::paintEvent(a0);
  }
#endif  // QT_CONFIG(splitter)

#if QT_CONFIG(splitter)
  //  void QSplitterHandle::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplitterHandleCall2 call = reinterpret_cast<CuteQSplitterHandleCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitterHandle::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(splitter)

#if QT_CONFIG(splitter)
  //  void QSplitterHandle::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplitterHandleCall3 call = reinterpret_cast<CuteQSplitterHandleCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitterHandle::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(splitter)

#if QT_CONFIG(splitter)
  //  void QSplitterHandle::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplitterHandleCall4 call = reinterpret_cast<CuteQSplitterHandleCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitterHandle::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(splitter)

#if QT_CONFIG(splitter)
  //  void QSplitterHandle::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplitterHandleCall5 call = reinterpret_cast<CuteQSplitterHandleCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSplitterHandle::resizeEvent(a0);
  }
#endif  // QT_CONFIG(splitter)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(splitter)
  //  bool QSplitterHandle::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplitterHandleCall6 call = reinterpret_cast<CuteQSplitterHandleCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSplitterHandle::event(a0);
  }
#endif  // QT_CONFIG(splitter)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplitterHandleCall7 call = reinterpret_cast<CuteQSplitterHandleCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplitterHandleCall8 call = reinterpret_cast<CuteQSplitterHandleCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplitterHandleCall9 call = reinterpret_cast<CuteQSplitterHandleCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplitterHandleCall10 call = reinterpret_cast<CuteQSplitterHandleCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplitterHandleCall11 call = reinterpret_cast<CuteQSplitterHandleCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSplitterHandleCall12 call = reinterpret_cast<CuteQSplitterHandleCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSplitterHandleCall13 call = reinterpret_cast<CuteQSplitterHandleCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSplitterHandleCall14 call = reinterpret_cast<CuteQSplitterHandleCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSplitterHandleCall15 call = reinterpret_cast<CuteQSplitterHandleCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSplitterHandleCall16 call = reinterpret_cast<CuteQSplitterHandleCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSplitterHandleCall17 call = reinterpret_cast<CuteQSplitterHandleCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSplitterHandleCall18 call = reinterpret_cast<CuteQSplitterHandleCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSplitterHandleCall19 call = reinterpret_cast<CuteQSplitterHandleCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSplitterHandleCall20 call = reinterpret_cast<CuteQSplitterHandleCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSplitterHandleCall21 call = reinterpret_cast<CuteQSplitterHandleCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSplitterHandleCall22 call = reinterpret_cast<CuteQSplitterHandleCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSplitterHandleCall23 call = reinterpret_cast<CuteQSplitterHandleCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSplitterHandleCall24 call = reinterpret_cast<CuteQSplitterHandleCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSplitterHandleCall25 call = reinterpret_cast<CuteQSplitterHandleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSplitterHandleCall26 call = reinterpret_cast<CuteQSplitterHandleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSplitterHandleCall27 call = reinterpret_cast<CuteQSplitterHandleCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSplitterHandleCall28 call = reinterpret_cast<CuteQSplitterHandleCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSplitterHandleCall29 call = reinterpret_cast<CuteQSplitterHandleCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSplitterHandleCall30 call = reinterpret_cast<CuteQSplitterHandleCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSplitterHandleCall31 call = reinterpret_cast<CuteQSplitterHandleCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSplitterHandleCall32 call = reinterpret_cast<CuteQSplitterHandleCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQSplitterHandleCall33 call = reinterpret_cast<CuteQSplitterHandleCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQSplitterHandleCall34 call = reinterpret_cast<CuteQSplitterHandleCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQSplitterHandleCall35 call = reinterpret_cast<CuteQSplitterHandleCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSplitterHandleCall36 call = reinterpret_cast<CuteQSplitterHandleCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQSplitterHandleCall37 call = reinterpret_cast<CuteQSplitterHandleCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSplitterHandleCall38 call = reinterpret_cast<CuteQSplitterHandleCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQSplitterHandleCall39 call = reinterpret_cast<CuteQSplitterHandleCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSplitterHandleCall40 call = reinterpret_cast<CuteQSplitterHandleCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQSplitterHandleCall41 call = reinterpret_cast<CuteQSplitterHandleCall41>(taken[41]);
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
      CuteQSplitterHandleCall42 call = reinterpret_cast<CuteQSplitterHandleCall42>(taken[42]);
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
      CuteQSplitterHandleCall43 call = reinterpret_cast<CuteQSplitterHandleCall43>(taken[43]);
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
      CuteQSplitterHandleCall44 call = reinterpret_cast<CuteQSplitterHandleCall44>(taken[44]);
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
      CuteQSplitterHandleCall45 call = reinterpret_cast<CuteQSplitterHandleCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSplitterHandle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSplitterHandle10metaObjectEv(
    const QSplitterHandle *self) {
  return self->metaObject();
}

//  void *QSplitterHandle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QSplitterHandle11qt_metacastEPKc(
    QSplitterHandle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSplitterHandle::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QSplitterHandle11qt_metacallEN11QMetaObject4CallEiPPv(
    QSplitterHandle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSplitterHandle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSplitterHandle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplitterHandle::tr(s, c, n));
}

//  QSplitterHandle::QSplitterHandle(Qt::Orientation o, QSplitter *parent)
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_ZN15QSplitterHandleC1EN2Qt11OrientationEP9QSplitter(
    Qt::Orientation o,
    QSplitter *parent) {
  return new CuteQSplitterHandle(o, parent);
}

//  QSplitterHandle::~QSplitterHandle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandleD1Ev(QSplitterHandle *self) {
  delete self;
}

//  void QSplitterHandle::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle14setOrientationEN2Qt11OrientationE(
    QSplitterHandle *self,
    Qt::Orientation o) {
  self->setOrientation(o);
}

//  Qt::Orientation QSplitterHandle::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QSplitterHandle11orientationEv(
    const QSplitterHandle *self) {
  return self->orientation();
}

//  bool QSplitterHandle::opaqueResize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSplitterHandle12opaqueResizeEv(
    const QSplitterHandle *self) {
  return self->opaqueResize();
}

//  QSplitter *QSplitterHandle::splitter() const
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZNK15QSplitterHandle8splitterEv(
    const QSplitterHandle *self) {
  return self->splitter();
}

//  QSize QSplitterHandle::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QSplitterHandle8sizeHintEv(const QSplitterHandle *self) {
  return new QSize(self->sizeHint());
}

//  void QSplitterHandle::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle10paintEventEP11QPaintEvent(
    QSplitterHandle *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QSplitterHandle::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle14mouseMoveEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QSplitterHandle::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle15mousePressEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QSplitterHandle::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle17mouseReleaseEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QSplitterHandle::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle11resizeEventEP12QResizeEvent(
    QSplitterHandle *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  bool QSplitterHandle::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QSplitterHandle5eventEP6QEvent(
    QSplitterHandle *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QSplitterHandle::moveSplitter(int p)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSplitterHandle12moveSplitterEi(
    QSplitterHandle *self,
    int p) {
  self->moveSplitter(p);
}

//  int QSplitterHandle::closestLegalPosition(int p)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QSplitterHandle20closestLegalPositionEi(
    QSplitterHandle *self,
    int p) {
  return self->closestLegalPosition(p);
}

//  QSplitterHandlePrivate *QSplitterHandle::d_func()
extern "C" Q_DECL_EXPORT
QSplitterHandlePrivate *ritual_ZN15QSplitterHandle6d_funcEv(
    QSplitterHandle *self) {
  return self->d_func();
}

//  const QSplitterHandlePrivate *QSplitterHandle::d_func() const
extern "C" Q_DECL_EXPORT
const QSplitterHandlePrivate *ritual_ZNK15QSplitterHandle6d_funcEv(
    const QSplitterHandle *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSplitterHandle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplitterHandle(
    QSplitterHandle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSplitterHandle *>(self)->take(key, call);
}

//  QSize QSplitterHandle::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QSplitterHandle8sizeHintEv(
    const QSplitterHandle *self) {
  return new QSize(self->QSplitterHandle::sizeHint());
}

//  void QSplitterHandle::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSplitterHandle10paintEventEP11QPaintEvent(
    QSplitterHandle *self,
    QPaintEvent *a0) {
  static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::paintEvent(
      a0);
}

//  void QSplitterHandle::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSplitterHandle14mouseMoveEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::mouseMoveEvent(
      a0);
}

//  void QSplitterHandle::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSplitterHandle15mousePressEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::mousePressEvent(
      a0);
}

//  void QSplitterHandle::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSplitterHandle17mouseReleaseEventEP11QMouseEvent(
    QSplitterHandle *self,
    QMouseEvent *a0) {
  static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::mouseReleaseEvent(
      a0);
}

//  void QSplitterHandle::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QSplitterHandle11resizeEventEP12QResizeEvent(
    QSplitterHandle *self,
    QResizeEvent *a0) {
  static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::resizeEvent(
      a0);
}

//  bool QSplitterHandle::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QSplitterHandle5eventEP6QEvent(
    QSplitterHandle *self,
    QEvent *a0) {
  return static_cast<OwnQSplitterHandle *>(self)->OwnQSplitterHandle::event(
      a0);
}

#endif  // QT_CONFIG(splitter)
#endif  // QT_CONFIG(splitter)
