//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwindowcontainer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwindowcontainer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWindowContainer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWindowContainer : QWindowContainer {
  using QWindowContainer::event;
  using QWindowContainer::eventFilter;
};

//  A QWindowContainer that Python can take functions over in. Every QWindowContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQWindowContainerCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowContainerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowContainerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQWindowContainerCall3)(const void *, int *);
typedef void (*CuteQWindowContainerCall4)(const void *, bool, int *);
typedef const QSize * (*CuteQWindowContainerCall5)(const void *, int *);
typedef int (*CuteQWindowContainerCall6)(const void *, int, int *);
typedef bool (*CuteQWindowContainerCall7)(const void *, int *);
typedef void * (*CuteQWindowContainerCall8)(const void *, int *);
typedef void (*CuteQWindowContainerCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowContainerCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowContainerCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowContainerCall12)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWindowContainerCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWindowContainerCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWindowContainerCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWindowContainerCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWindowContainerCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWindowContainerCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWindowContainerCall19)(const void *, QEvent *, int *);
typedef void (*CuteQWindowContainerCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWindowContainerCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWindowContainerCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWindowContainerCall23)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQWindowContainerCall24)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWindowContainerCall25)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQWindowContainerCall26)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWindowContainerCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWindowContainerCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWindowContainerCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWindowContainerCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQWindowContainerCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQWindowContainerCall32)(const void *, QHideEvent *, int *);
typedef void (*CuteQWindowContainerCall33)(const void *, QEvent *, int *);
typedef int (*CuteQWindowContainerCall34)(const void *, int, int *);
typedef void (*CuteQWindowContainerCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQWindowContainerCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQWindowContainerCall37)(const void *, int *);
typedef void (*CuteQWindowContainerCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWindowContainerCall39)(const void *, int, int *);
typedef bool (*CuteQWindowContainerCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowContainerCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowContainerCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowContainerCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowContainerCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowContainerCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowContainer : public QWindowContainer {
public:
  using QWindowContainer::QWindowContainer;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[23] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[32] = call;
      return true;
    }
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

  //  QSize QWindowContainer::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowContainerCall0 call = reinterpret_cast<CuteQWindowContainerCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowContainer::minimumSizeHint();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWindowContainer::event(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowContainerCall1 call = reinterpret_cast<CuteQWindowContainerCall1>(taken[1]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QWindowContainer::event(ev);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QWindowContainer::eventFilter(QObject *a0, QEvent *ev)
  bool eventFilter(QObject *a0, QEvent *ev) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowContainerCall2 call = reinterpret_cast<CuteQWindowContainerCall2>(taken[2]);
      bool given = call(this, a0, ev, &handled);
      if (handled) return given;
    }
    return QWindowContainer::eventFilter(a0, ev);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowContainerCall3 call = reinterpret_cast<CuteQWindowContainerCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowContainerCall4 call = reinterpret_cast<CuteQWindowContainerCall4>(taken[4]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowContainerCall5 call = reinterpret_cast<CuteQWindowContainerCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowContainerCall6 call = reinterpret_cast<CuteQWindowContainerCall6>(taken[6]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowContainerCall7 call = reinterpret_cast<CuteQWindowContainerCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowContainerCall8 call = reinterpret_cast<CuteQWindowContainerCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowContainerCall9 call = reinterpret_cast<CuteQWindowContainerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowContainerCall10 call = reinterpret_cast<CuteQWindowContainerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowContainerCall11 call = reinterpret_cast<CuteQWindowContainerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWindowContainerCall12 call = reinterpret_cast<CuteQWindowContainerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWindowContainerCall13 call = reinterpret_cast<CuteQWindowContainerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWindowContainerCall14 call = reinterpret_cast<CuteQWindowContainerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWindowContainerCall15 call = reinterpret_cast<CuteQWindowContainerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWindowContainerCall16 call = reinterpret_cast<CuteQWindowContainerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWindowContainerCall17 call = reinterpret_cast<CuteQWindowContainerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWindowContainerCall18 call = reinterpret_cast<CuteQWindowContainerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWindowContainerCall19 call = reinterpret_cast<CuteQWindowContainerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWindowContainerCall20 call = reinterpret_cast<CuteQWindowContainerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWindowContainerCall21 call = reinterpret_cast<CuteQWindowContainerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWindowContainerCall22 call = reinterpret_cast<CuteQWindowContainerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWindowContainerCall23 call = reinterpret_cast<CuteQWindowContainerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWindowContainerCall24 call = reinterpret_cast<CuteQWindowContainerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWindowContainerCall25 call = reinterpret_cast<CuteQWindowContainerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWindowContainerCall26 call = reinterpret_cast<CuteQWindowContainerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWindowContainerCall27 call = reinterpret_cast<CuteQWindowContainerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWindowContainerCall28 call = reinterpret_cast<CuteQWindowContainerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWindowContainerCall29 call = reinterpret_cast<CuteQWindowContainerCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWindowContainerCall30 call = reinterpret_cast<CuteQWindowContainerCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWindowContainerCall31 call = reinterpret_cast<CuteQWindowContainerCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWindowContainerCall32 call = reinterpret_cast<CuteQWindowContainerCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWindowContainerCall33 call = reinterpret_cast<CuteQWindowContainerCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQWindowContainerCall34 call = reinterpret_cast<CuteQWindowContainerCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQWindowContainerCall35 call = reinterpret_cast<CuteQWindowContainerCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQWindowContainerCall36 call = reinterpret_cast<CuteQWindowContainerCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQWindowContainerCall37 call = reinterpret_cast<CuteQWindowContainerCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQWindowContainerCall38 call = reinterpret_cast<CuteQWindowContainerCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQWindowContainerCall39 call = reinterpret_cast<CuteQWindowContainerCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWindowContainerCall40 call = reinterpret_cast<CuteQWindowContainerCall40>(taken[40]);
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
      CuteQWindowContainerCall41 call = reinterpret_cast<CuteQWindowContainerCall41>(taken[41]);
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
      CuteQWindowContainerCall42 call = reinterpret_cast<CuteQWindowContainerCall42>(taken[42]);
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
      CuteQWindowContainerCall43 call = reinterpret_cast<CuteQWindowContainerCall43>(taken[43]);
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
      CuteQWindowContainerCall44 call = reinterpret_cast<CuteQWindowContainerCall44>(taken[44]);
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
      CuteQWindowContainerCall45 call = reinterpret_cast<CuteQWindowContainerCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowContainer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QWindowContainer10metaObjectEv(
    const QWindowContainer *self) {
  return self->metaObject();
}

//  void *QWindowContainer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QWindowContainer11qt_metacastEPKc(
    QWindowContainer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWindowContainer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QWindowContainer11qt_metacallEN11QMetaObject4CallEiPPv(
    QWindowContainer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWindowContainer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWindowContainer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowContainer::tr(s, c, n));
}

//  QWindowContainerPrivate *QWindowContainer::d_func()
extern "C" Q_DECL_EXPORT
QWindowContainerPrivate *ritual_ZN16QWindowContainer6d_funcEv(
    QWindowContainer *self) {
  return self->d_func();
}

//  const QWindowContainerPrivate *QWindowContainer::d_func() const
extern "C" Q_DECL_EXPORT
const QWindowContainerPrivate *ritual_ZNK16QWindowContainer6d_funcEv(
    const QWindowContainer *self) {
  return self->d_func();
}

//  QWindowContainer::QWindowContainer(QWindow *embeddedWindow, QWidget
//      *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QWindowContainer *ritual_ZN16QWindowContainerC1EP7QWindowP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWindow *embeddedWindow,
    QWidget *parent,
    int f) {
  return new CuteQWindowContainer(
      embeddedWindow,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  QWindowContainer::~QWindowContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainerD1Ev(QWindowContainer *self) {
  delete self;
}

//  QWindow *QWindowContainer::containedWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK16QWindowContainer15containedWindowEv(
    const QWindowContainer *self) {
  return self->containedWindow();
}

//  QSize QWindowContainer::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QWindowContainer15minimumSizeHintEv(
    const QWindowContainer *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QWindowContainer::toplevelAboutToBeDestroyed(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainer26toplevelAboutToBeDestroyedEP7QWidget(
    QWidget *parent) {
  QWindowContainer::toplevelAboutToBeDestroyed(parent);
}

//  void QWindowContainer::parentWasChanged(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainer16parentWasChangedEP7QWidget(
    QWidget *parent) {
  QWindowContainer::parentWasChanged(parent);
}

//  void QWindowContainer::parentWasMoved(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainer14parentWasMovedEP7QWidget(QWidget *parent) {
  QWindowContainer::parentWasMoved(parent);
}

//  void QWindowContainer::parentWasRaised(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainer15parentWasRaisedEP7QWidget(
    QWidget *parent) {
  QWindowContainer::parentWasRaised(parent);
}

//  void QWindowContainer::parentWasLowered(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWindowContainer16parentWasLoweredEP7QWidget(
    QWidget *parent) {
  QWindowContainer::parentWasLowered(parent);
}

//  bool QWindowContainer::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QWindowContainer5eventEP6QEvent(
    QWindowContainer *self,
    QEvent *ev) {
  return self->event(ev);
}

//  bool QWindowContainer::eventFilter(QObject *a0, QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QWindowContainer11eventFilterEP7QObjectP6QEvent(
    QWindowContainer *self,
    QObject *a0,
    QEvent *ev) {
  return self->eventFilter(a0, ev);
}

//  a Python function taken by a CuteQWindowContainer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowContainer(
    QWindowContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowContainer *>(self)->take(key, call);
}

//  QSize QWindowContainer::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK16QWindowContainer15minimumSizeHintEv(
    const QWindowContainer *self) {
  return new QSize(self->QWindowContainer::minimumSizeHint());
}

//  bool QWindowContainer::event(QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QWindowContainer5eventEP6QEvent(
    QWindowContainer *self,
    QEvent *ev) {
  return static_cast<OwnQWindowContainer *>(self)->OwnQWindowContainer::event(
      ev);
}

//  bool QWindowContainer::eventFilter(QObject *a0, QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QWindowContainer11eventFilterEP7QObjectP6QEvent(
    QWindowContainer *self,
    QObject *a0,
    QEvent *ev) {
  return static_cast<OwnQWindowContainer *>(self)->OwnQWindowContainer::eventFilter(
      a0,
      ev);
}
