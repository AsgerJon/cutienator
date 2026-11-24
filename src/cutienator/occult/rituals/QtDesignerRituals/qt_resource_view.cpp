//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qtresourceview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qtresourceview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtResourceView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtResourceView : QtResourceView {
  using QtResourceView::event;
};

//  A QtResourceView that Python can take functions over in. Every QtResourceView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtResourceViewCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQtResourceViewCall1)(const void *, int *);
typedef void (*CuteQtResourceViewCall2)(const void *, bool, int *);
typedef const QSize * (*CuteQtResourceViewCall3)(const void *, int *);
typedef const QSize * (*CuteQtResourceViewCall4)(const void *, int *);
typedef int (*CuteQtResourceViewCall5)(const void *, int, int *);
typedef bool (*CuteQtResourceViewCall6)(const void *, int *);
typedef void * (*CuteQtResourceViewCall7)(const void *, int *);
typedef void (*CuteQtResourceViewCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtResourceViewCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtResourceViewCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtResourceViewCall11)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQtResourceViewCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQtResourceViewCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtResourceViewCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtResourceViewCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQtResourceViewCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQtResourceViewCall17)(const void *, QEnterEvent *, int *);
typedef void (*CuteQtResourceViewCall18)(const void *, QEvent *, int *);
typedef void (*CuteQtResourceViewCall19)(const void *, QPaintEvent *, int *);
typedef void (*CuteQtResourceViewCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQtResourceViewCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQtResourceViewCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQtResourceViewCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQtResourceViewCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQtResourceViewCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtResourceViewCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtResourceViewCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtResourceViewCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtResourceViewCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQtResourceViewCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQtResourceViewCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQtResourceViewCall32)(const void *, QEvent *, int *);
typedef int (*CuteQtResourceViewCall33)(const void *, int, int *);
typedef void (*CuteQtResourceViewCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQtResourceViewCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQtResourceViewCall36)(const void *, int *);
typedef void (*CuteQtResourceViewCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQtResourceViewCall38)(const void *, int, int *);
typedef bool (*CuteQtResourceViewCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtResourceViewCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceViewCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceViewCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceViewCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceViewCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtResourceViewCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtResourceView : public QtResourceView {
public:
  using QtResourceView::QtResourceView;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
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

#if !defined(QT_NO_QOBJECT)
  //  bool QtResourceView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtResourceViewCall0 call = reinterpret_cast<CuteQtResourceViewCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QtResourceView::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtResourceViewCall1 call = reinterpret_cast<CuteQtResourceViewCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtResourceViewCall2 call = reinterpret_cast<CuteQtResourceViewCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtResourceViewCall3 call = reinterpret_cast<CuteQtResourceViewCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQtResourceViewCall4 call = reinterpret_cast<CuteQtResourceViewCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtResourceViewCall5 call = reinterpret_cast<CuteQtResourceViewCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQtResourceViewCall6 call = reinterpret_cast<CuteQtResourceViewCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQtResourceViewCall7 call = reinterpret_cast<CuteQtResourceViewCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtResourceViewCall8 call = reinterpret_cast<CuteQtResourceViewCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtResourceViewCall9 call = reinterpret_cast<CuteQtResourceViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtResourceViewCall10 call = reinterpret_cast<CuteQtResourceViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtResourceViewCall11 call = reinterpret_cast<CuteQtResourceViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtResourceViewCall12 call = reinterpret_cast<CuteQtResourceViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtResourceViewCall13 call = reinterpret_cast<CuteQtResourceViewCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtResourceViewCall14 call = reinterpret_cast<CuteQtResourceViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtResourceViewCall15 call = reinterpret_cast<CuteQtResourceViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtResourceViewCall16 call = reinterpret_cast<CuteQtResourceViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQtResourceViewCall17 call = reinterpret_cast<CuteQtResourceViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtResourceViewCall18 call = reinterpret_cast<CuteQtResourceViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQtResourceViewCall19 call = reinterpret_cast<CuteQtResourceViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQtResourceViewCall20 call = reinterpret_cast<CuteQtResourceViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQtResourceViewCall21 call = reinterpret_cast<CuteQtResourceViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQtResourceViewCall22 call = reinterpret_cast<CuteQtResourceViewCall22>(taken[22]);
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
      CuteQtResourceViewCall23 call = reinterpret_cast<CuteQtResourceViewCall23>(taken[23]);
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
      CuteQtResourceViewCall24 call = reinterpret_cast<CuteQtResourceViewCall24>(taken[24]);
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
      CuteQtResourceViewCall25 call = reinterpret_cast<CuteQtResourceViewCall25>(taken[25]);
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
      CuteQtResourceViewCall26 call = reinterpret_cast<CuteQtResourceViewCall26>(taken[26]);
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
      CuteQtResourceViewCall27 call = reinterpret_cast<CuteQtResourceViewCall27>(taken[27]);
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
      CuteQtResourceViewCall28 call = reinterpret_cast<CuteQtResourceViewCall28>(taken[28]);
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
      CuteQtResourceViewCall29 call = reinterpret_cast<CuteQtResourceViewCall29>(taken[29]);
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
      CuteQtResourceViewCall30 call = reinterpret_cast<CuteQtResourceViewCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQtResourceViewCall31 call = reinterpret_cast<CuteQtResourceViewCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQtResourceViewCall32 call = reinterpret_cast<CuteQtResourceViewCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQtResourceViewCall33 call = reinterpret_cast<CuteQtResourceViewCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQtResourceViewCall34 call = reinterpret_cast<CuteQtResourceViewCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQtResourceViewCall35 call = reinterpret_cast<CuteQtResourceViewCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQtResourceViewCall36 call = reinterpret_cast<CuteQtResourceViewCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQtResourceViewCall37 call = reinterpret_cast<CuteQtResourceViewCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQtResourceViewCall38 call = reinterpret_cast<CuteQtResourceViewCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQtResourceViewCall39 call = reinterpret_cast<CuteQtResourceViewCall39>(taken[39]);
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
      CuteQtResourceViewCall40 call = reinterpret_cast<CuteQtResourceViewCall40>(taken[40]);
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
      CuteQtResourceViewCall41 call = reinterpret_cast<CuteQtResourceViewCall41>(taken[41]);
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
      CuteQtResourceViewCall42 call = reinterpret_cast<CuteQtResourceViewCall42>(taken[42]);
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
      CuteQtResourceViewCall43 call = reinterpret_cast<CuteQtResourceViewCall43>(taken[43]);
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
      CuteQtResourceViewCall44 call = reinterpret_cast<CuteQtResourceViewCall44>(taken[44]);
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
      CuteQtResourceViewCall45 call = reinterpret_cast<CuteQtResourceViewCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtResourceView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QtResourceView10metaObjectEv(
    const QtResourceView *self) {
  return self->metaObject();
}

//  QString QtResourceView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QtResourceView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtResourceView::tr(s, c, n));
}

//  QtResourceView::QtResourceView(QDesignerFormEditorInterface *core,
//      QWidget *parent)
extern "C" Q_DECL_EXPORT
QtResourceView *ritual_ZN14QtResourceViewC1EP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerFormEditorInterface *core,
    QWidget *parent) {
  return new CuteQtResourceView(core, parent);
}

//  QtResourceView::~QtResourceView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceViewD1Ev(QtResourceView *self) {
  delete self;
}

//  void QtResourceView::setDragEnabled(bool dragEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceView14setDragEnabledEb(
    QtResourceView *self,
    bool dragEnabled) {
  self->setDragEnabled(dragEnabled);
}

//  bool QtResourceView::dragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QtResourceView11dragEnabledEv(const QtResourceView *self) {
  return self->dragEnabled();
}

//  QtResourceModel *QtResourceView::model() const
extern "C" Q_DECL_EXPORT
QtResourceModel *ritual_ZNK14QtResourceView5modelEv(
    const QtResourceView *self) {
  return self->model();
}

//  void QtResourceView::setResourceModel(QtResourceModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceView16setResourceModelEP15QtResourceModel(
    QtResourceView *self,
    QtResourceModel *model) {
  self->setResourceModel(model);
}

//  QString QtResourceView::selectedResource() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QtResourceView16selectedResourceEv(
    const QtResourceView *self) {
  return new QString(self->selectedResource());
}

//  void QtResourceView::selectResource(const QString &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceView14selectResourceERK7QString(
    QtResourceView *self,
    const QString *resource) {
  self->selectResource(*resource);
}

//  QString QtResourceView::settingsKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QtResourceView11settingsKeyEv(
    const QtResourceView *self) {
  return new QString(self->settingsKey());
}

//  void QtResourceView::setSettingsKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceView14setSettingsKeyERK7QString(
    QtResourceView *self,
    const QString *key) {
  self->setSettingsKey(*key);
}

//  bool QtResourceView::isResourceEditingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QtResourceView24isResourceEditingEnabledEv(
    const QtResourceView *self) {
  return self->isResourceEditingEnabled();
}

//  void QtResourceView::setResourceEditingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QtResourceView25setResourceEditingEnabledEb(
    QtResourceView *self,
    bool enable) {
  self->setResourceEditingEnabled(enable);
}

//  QString QtResourceView::encodeMimeData(ResourceType resourceType, const
//      QString &path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QtResourceView14encodeMimeDataENS_12ResourceTypeERK7QString(
    QtResourceView::ResourceType resourceType,
    const QString *path) {
  return new QString(QtResourceView::encodeMimeData(resourceType, *path));
}

//  bool QtResourceView::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QtResourceView5eventEP6QEvent(
    QtResourceView *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQtResourceView, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtResourceView(
    QtResourceView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtResourceView *>(self)->take(key, call);
}

//  bool QtResourceView::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QtResourceView5eventEP6QEvent(
    QtResourceView *self,
    QEvent *event) {
  return static_cast<OwnQtResourceView *>(self)->OwnQtResourceView::event(
      event);
}
