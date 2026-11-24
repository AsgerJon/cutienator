//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaWidgets/qvideowidget.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtMultimediaWidgets/qvideowidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QVideoWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVideoWidget : QVideoWidget {
  using QVideoWidget::event;
  using QVideoWidget::showEvent;
  using QVideoWidget::hideEvent;
  using QVideoWidget::resizeEvent;
  using QVideoWidget::moveEvent;
};

//  A QVideoWidget that Python can take functions over in. Every QVideoWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQVideoWidgetCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoWidgetCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall2)(const void *, QShowEvent *, int *);
typedef void (*CuteQVideoWidgetCall3)(const void *, QHideEvent *, int *);
typedef void (*CuteQVideoWidgetCall4)(const void *, QResizeEvent *, int *);
typedef void (*CuteQVideoWidgetCall5)(const void *, QMoveEvent *, int *);
typedef int (*CuteQVideoWidgetCall6)(const void *, int *);
typedef void (*CuteQVideoWidgetCall7)(const void *, bool, int *);
typedef const QSize * (*CuteQVideoWidgetCall8)(const void *, int *);
typedef int (*CuteQVideoWidgetCall9)(const void *, int, int *);
typedef bool (*CuteQVideoWidgetCall10)(const void *, int *);
typedef void * (*CuteQVideoWidgetCall11)(const void *, int *);
typedef void (*CuteQVideoWidgetCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQVideoWidgetCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQVideoWidgetCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQVideoWidgetCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVideoWidgetCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQVideoWidgetCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVideoWidgetCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQVideoWidgetCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQVideoWidgetCall22)(const void *, QEvent *, int *);
typedef void (*CuteQVideoWidgetCall23)(const void *, QPaintEvent *, int *);
typedef void (*CuteQVideoWidgetCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQVideoWidgetCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQVideoWidgetCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQVideoWidgetCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQVideoWidgetCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQVideoWidgetCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQVideoWidgetCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQVideoWidgetCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQVideoWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQVideoWidgetCall33)(const void *, int, int *);
typedef void (*CuteQVideoWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQVideoWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQVideoWidgetCall36)(const void *, int *);
typedef void (*CuteQVideoWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQVideoWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQVideoWidgetCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoWidgetCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVideoWidget : public QVideoWidget {
public:
  using QVideoWidget::QVideoWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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

  //  QSize QVideoWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVideoWidgetCall0 call = reinterpret_cast<CuteQVideoWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVideoWidget::sizeHint();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QVideoWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVideoWidgetCall1 call = reinterpret_cast<CuteQVideoWidgetCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QVideoWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QVideoWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVideoWidgetCall2 call = reinterpret_cast<CuteQVideoWidgetCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QVideoWidget::showEvent(event);
  }

  //  void QVideoWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVideoWidgetCall3 call = reinterpret_cast<CuteQVideoWidgetCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QVideoWidget::hideEvent(event);
  }

  //  void QVideoWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQVideoWidgetCall4 call = reinterpret_cast<CuteQVideoWidgetCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QVideoWidget::resizeEvent(event);
  }

  //  void QVideoWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQVideoWidgetCall5 call = reinterpret_cast<CuteQVideoWidgetCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QVideoWidget::moveEvent(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVideoWidgetCall6 call = reinterpret_cast<CuteQVideoWidgetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[7]) {
      int handled = 0;
      CuteQVideoWidgetCall7 call = reinterpret_cast<CuteQVideoWidgetCall7>(taken[7]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQVideoWidgetCall8 call = reinterpret_cast<CuteQVideoWidgetCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQVideoWidgetCall9 call = reinterpret_cast<CuteQVideoWidgetCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQVideoWidgetCall10 call = reinterpret_cast<CuteQVideoWidgetCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQVideoWidgetCall11 call = reinterpret_cast<CuteQVideoWidgetCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQVideoWidgetCall12 call = reinterpret_cast<CuteQVideoWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQVideoWidgetCall13 call = reinterpret_cast<CuteQVideoWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQVideoWidgetCall14 call = reinterpret_cast<CuteQVideoWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQVideoWidgetCall15 call = reinterpret_cast<CuteQVideoWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQVideoWidgetCall16 call = reinterpret_cast<CuteQVideoWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQVideoWidgetCall17 call = reinterpret_cast<CuteQVideoWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQVideoWidgetCall18 call = reinterpret_cast<CuteQVideoWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQVideoWidgetCall19 call = reinterpret_cast<CuteQVideoWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQVideoWidgetCall20 call = reinterpret_cast<CuteQVideoWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQVideoWidgetCall21 call = reinterpret_cast<CuteQVideoWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQVideoWidgetCall22 call = reinterpret_cast<CuteQVideoWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQVideoWidgetCall23 call = reinterpret_cast<CuteQVideoWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQVideoWidgetCall24 call = reinterpret_cast<CuteQVideoWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQVideoWidgetCall25 call = reinterpret_cast<CuteQVideoWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQVideoWidgetCall26 call = reinterpret_cast<CuteQVideoWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQVideoWidgetCall27 call = reinterpret_cast<CuteQVideoWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQVideoWidgetCall28 call = reinterpret_cast<CuteQVideoWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQVideoWidgetCall29 call = reinterpret_cast<CuteQVideoWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQVideoWidgetCall30 call = reinterpret_cast<CuteQVideoWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQVideoWidgetCall31 call = reinterpret_cast<CuteQVideoWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQVideoWidgetCall32 call = reinterpret_cast<CuteQVideoWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQVideoWidgetCall33 call = reinterpret_cast<CuteQVideoWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQVideoWidgetCall34 call = reinterpret_cast<CuteQVideoWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQVideoWidgetCall35 call = reinterpret_cast<CuteQVideoWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQVideoWidgetCall36 call = reinterpret_cast<CuteQVideoWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQVideoWidgetCall37 call = reinterpret_cast<CuteQVideoWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQVideoWidgetCall38 call = reinterpret_cast<CuteQVideoWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQVideoWidgetCall39 call = reinterpret_cast<CuteQVideoWidgetCall39>(taken[39]);
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
      CuteQVideoWidgetCall40 call = reinterpret_cast<CuteQVideoWidgetCall40>(taken[40]);
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
      CuteQVideoWidgetCall41 call = reinterpret_cast<CuteQVideoWidgetCall41>(taken[41]);
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
      CuteQVideoWidgetCall42 call = reinterpret_cast<CuteQVideoWidgetCall42>(taken[42]);
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
      CuteQVideoWidgetCall43 call = reinterpret_cast<CuteQVideoWidgetCall43>(taken[43]);
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
      CuteQVideoWidgetCall44 call = reinterpret_cast<CuteQVideoWidgetCall44>(taken[44]);
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
      CuteQVideoWidgetCall45 call = reinterpret_cast<CuteQVideoWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVideoWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QVideoWidget10metaObjectEv(
    const QVideoWidget *self) {
  return self->metaObject();
}

//  QString QVideoWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QVideoWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVideoWidget::tr(s, c, n));
}

//  QVideoWidget::QVideoWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QVideoWidget *ritual_ZN12QVideoWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQVideoWidget(parent);
}

//  QVideoWidget::~QVideoWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidgetD1Ev(QVideoWidget *self) {
  delete self;
}

//  QVideoSink *QVideoWidget::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK12QVideoWidget9videoSinkEv(const QVideoWidget *self) {
  return self->videoSink();
}

//  Qt::AspectRatioMode QVideoWidget::aspectRatioMode() const
extern "C" Q_DECL_EXPORT
Qt::AspectRatioMode ritual_ZNK12QVideoWidget15aspectRatioModeEv(
    const QVideoWidget *self) {
  return self->aspectRatioMode();
}

//  QSize QVideoWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QVideoWidget8sizeHintEv(const QVideoWidget *self) {
  return new QSize(self->sizeHint());
}

//  void QVideoWidget::setFullScreen(bool fullScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget13setFullScreenEb(
    QVideoWidget *self,
    bool fullScreen) {
  self->setFullScreen(fullScreen);
}

//  void QVideoWidget::setAspectRatioMode(Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QVideoWidget *self,
    Qt::AspectRatioMode mode) {
  self->setAspectRatioMode(mode);
}

//  bool QVideoWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QVideoWidget5eventEP6QEvent(
    QVideoWidget *self,
    QEvent *event) {
  return self->event(event);
}

//  void QVideoWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget9showEventEP10QShowEvent(
    QVideoWidget *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QVideoWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget9hideEventEP10QHideEvent(
    QVideoWidget *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void QVideoWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget11resizeEventEP12QResizeEvent(
    QVideoWidget *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QVideoWidget::moveEvent(QMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVideoWidget9moveEventEP10QMoveEvent(
    QVideoWidget *self,
    QMoveEvent *event) {
  self->moveEvent(event);
}

//  QVideoWidgetPrivate *QVideoWidget::d_func()
extern "C" Q_DECL_EXPORT
QVideoWidgetPrivate *ritual_ZN12QVideoWidget6d_funcEv(QVideoWidget *self) {
  return self->d_func();
}

//  const QVideoWidgetPrivate *QVideoWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QVideoWidgetPrivate *ritual_ZNK12QVideoWidget6d_funcEv(
    const QVideoWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQVideoWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoWidget(
    QVideoWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVideoWidget *>(self)->take(key, call);
}

//  QSize QVideoWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QVideoWidget8sizeHintEv(const QVideoWidget *self) {
  return new QSize(self->QVideoWidget::sizeHint());
}

//  bool QVideoWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QVideoWidget5eventEP6QEvent(
    QVideoWidget *self,
    QEvent *event) {
  return static_cast<OwnQVideoWidget *>(self)->OwnQVideoWidget::event(event);
}

//  void QVideoWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QVideoWidget9showEventEP10QShowEvent(
    QVideoWidget *self,
    QShowEvent *event) {
  static_cast<OwnQVideoWidget *>(self)->OwnQVideoWidget::showEvent(event);
}

//  void QVideoWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QVideoWidget9hideEventEP10QHideEvent(
    QVideoWidget *self,
    QHideEvent *event) {
  static_cast<OwnQVideoWidget *>(self)->OwnQVideoWidget::hideEvent(event);
}

//  void QVideoWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QVideoWidget11resizeEventEP12QResizeEvent(
    QVideoWidget *self,
    QResizeEvent *event) {
  static_cast<OwnQVideoWidget *>(self)->OwnQVideoWidget::resizeEvent(event);
}

//  void QVideoWidget::moveEvent(QMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QVideoWidget9moveEventEP10QMoveEvent(
    QVideoWidget *self,
    QMoveEvent *event) {
  static_cast<OwnQVideoWidget *>(self)->OwnQVideoWidget::moveEvent(event);
}
