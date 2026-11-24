//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QToolBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQToolBar : QToolBar {
  using QToolBar::actionEvent;
  using QToolBar::changeEvent;
  using QToolBar::paintEvent;
  using QToolBar::event;
  using QToolBar::initStyleOption;
};

//  A QToolBar that Python can take functions over in. Every QToolBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarCall0)(const void *, QActionEvent *, int *);
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarCall2)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(toolbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbar)
typedef bool (*CuteQToolBarCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarCall4)(const void *, QStyleOptionToolBar *, int *);
#endif  // QT_CONFIG(toolbar)
typedef int (*CuteQToolBarCall5)(const void *, int *);
typedef void (*CuteQToolBarCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQToolBarCall7)(const void *, int *);
typedef const QSize * (*CuteQToolBarCall8)(const void *, int *);
typedef int (*CuteQToolBarCall9)(const void *, int, int *);
typedef bool (*CuteQToolBarCall10)(const void *, int *);
typedef void * (*CuteQToolBarCall11)(const void *, int *);
typedef void (*CuteQToolBarCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQToolBarCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQToolBarCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBarCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBarCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBarCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBarCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQToolBarCall22)(const void *, QEvent *, int *);
typedef void (*CuteQToolBarCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQToolBarCall24)(const void *, QResizeEvent *, int *);
typedef void (*CuteQToolBarCall25)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQToolBarCall26)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQToolBarCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolBarCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolBarCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolBarCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQToolBarCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQToolBarCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQToolBarCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQToolBarCall34)(const void *, int, int *);
typedef void (*CuteQToolBarCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQToolBarCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQToolBarCall37)(const void *, int *);
typedef void (*CuteQToolBarCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQToolBarCall39)(const void *, int, int *);
typedef bool (*CuteQToolBarCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQToolBarCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQToolBar : public QToolBar {
public:
  using QToolBar::QToolBar;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_ACTION)
#if QT_CONFIG(toolbar)
  //  void QToolBar::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarCall0 call = reinterpret_cast<CuteQToolBarCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QToolBar::actionEvent(event);
  }
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(toolbar)
  //  void QToolBar::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarCall1 call = reinterpret_cast<CuteQToolBarCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QToolBar::changeEvent(event);
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  void QToolBar::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBarCall2 call = reinterpret_cast<CuteQToolBarCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QToolBar::paintEvent(event);
  }
#endif  // QT_CONFIG(toolbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(toolbar)
  //  bool QToolBar::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBarCall3 call = reinterpret_cast<CuteQToolBarCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QToolBar::event(event);
  }
#endif  // QT_CONFIG(toolbar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(toolbar)
  //  void QToolBar::initStyleOption(QStyleOptionToolBar *option) const
  void initStyleOption(QStyleOptionToolBar *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBarCall4 call = reinterpret_cast<CuteQToolBarCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QToolBar::initStyleOption(option);
  }
#endif  // QT_CONFIG(toolbar)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBarCall5 call = reinterpret_cast<CuteQToolBarCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBarCall6 call = reinterpret_cast<CuteQToolBarCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBarCall7 call = reinterpret_cast<CuteQToolBarCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBarCall8 call = reinterpret_cast<CuteQToolBarCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBarCall9 call = reinterpret_cast<CuteQToolBarCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBarCall10 call = reinterpret_cast<CuteQToolBarCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBarCall11 call = reinterpret_cast<CuteQToolBarCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBarCall12 call = reinterpret_cast<CuteQToolBarCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBarCall13 call = reinterpret_cast<CuteQToolBarCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBarCall14 call = reinterpret_cast<CuteQToolBarCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolBarCall15 call = reinterpret_cast<CuteQToolBarCall15>(taken[15]);
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
      CuteQToolBarCall16 call = reinterpret_cast<CuteQToolBarCall16>(taken[16]);
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
      CuteQToolBarCall17 call = reinterpret_cast<CuteQToolBarCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQToolBarCall18 call = reinterpret_cast<CuteQToolBarCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQToolBarCall19 call = reinterpret_cast<CuteQToolBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQToolBarCall20 call = reinterpret_cast<CuteQToolBarCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQToolBarCall21 call = reinterpret_cast<CuteQToolBarCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQToolBarCall22 call = reinterpret_cast<CuteQToolBarCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQToolBarCall23 call = reinterpret_cast<CuteQToolBarCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQToolBarCall24 call = reinterpret_cast<CuteQToolBarCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQToolBarCall25 call = reinterpret_cast<CuteQToolBarCall25>(taken[25]);
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
      CuteQToolBarCall26 call = reinterpret_cast<CuteQToolBarCall26>(taken[26]);
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
      CuteQToolBarCall27 call = reinterpret_cast<CuteQToolBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQToolBarCall28 call = reinterpret_cast<CuteQToolBarCall28>(taken[28]);
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
      CuteQToolBarCall29 call = reinterpret_cast<CuteQToolBarCall29>(taken[29]);
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
      CuteQToolBarCall30 call = reinterpret_cast<CuteQToolBarCall30>(taken[30]);
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
      CuteQToolBarCall31 call = reinterpret_cast<CuteQToolBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQToolBarCall32 call = reinterpret_cast<CuteQToolBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQToolBarCall33 call = reinterpret_cast<CuteQToolBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQToolBarCall34 call = reinterpret_cast<CuteQToolBarCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQToolBarCall35 call = reinterpret_cast<CuteQToolBarCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQToolBarCall36 call = reinterpret_cast<CuteQToolBarCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQToolBarCall37 call = reinterpret_cast<CuteQToolBarCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQToolBarCall38 call = reinterpret_cast<CuteQToolBarCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQToolBarCall39 call = reinterpret_cast<CuteQToolBarCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQToolBarCall40 call = reinterpret_cast<CuteQToolBarCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQToolBarCall41 call = reinterpret_cast<CuteQToolBarCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQToolBarCall42 call = reinterpret_cast<CuteQToolBarCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQToolBarCall43 call = reinterpret_cast<CuteQToolBarCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQToolBarCall44 call = reinterpret_cast<CuteQToolBarCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQToolBarCall45 call = reinterpret_cast<CuteQToolBarCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQToolBarCall46 call = reinterpret_cast<CuteQToolBarCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QToolBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QToolBar10metaObjectEv(const QToolBar *self) {
  return self->metaObject();
}

//  QString QToolBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QToolBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QToolBar::tr(s, c, n));
}

//  QToolBar::QToolBar(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN8QToolBarC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new CuteQToolBar(*title, parent);
}

//  QToolBar::QToolBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN8QToolBarC1EP7QWidget(QWidget *parent) {
  return new CuteQToolBar(parent);
}

//  QToolBar::~QToolBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBarD1Ev(QToolBar *self) {
  delete self;
}

//  void QToolBar::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar10setMovableEb(QToolBar *self, bool movable) {
  self->setMovable(movable);
}

//  bool QToolBar::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar9isMovableEv(const QToolBar *self) {
  return self->isMovable();
}

//  void QToolBar::setAllowedAreas(Qt::ToolBarAreas areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar15setAllowedAreasE6QFlagsIN2Qt11ToolBarAreaEE(
    QToolBar *self,
    int areas) {
  self->setAllowedAreas(QFlags<Qt::ToolBarArea>::fromInt(areas));
}

//  Qt::ToolBarAreas QToolBar::allowedAreas() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBar12allowedAreasEv(const QToolBar *self) {
  return static_cast<int>(self->allowedAreas().toInt());
}

//  bool QToolBar::isAreaAllowed(Qt::ToolBarArea area) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar13isAreaAllowedEN2Qt11ToolBarAreaE(
    const QToolBar *self,
    Qt::ToolBarArea area) {
  return self->isAreaAllowed(area);
}

//  void QToolBar::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar14setOrientationEN2Qt11OrientationE(
    QToolBar *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QToolBar::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK8QToolBar11orientationEv(const QToolBar *self) {
  return self->orientation();
}

//  void QToolBar::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar5clearEv(QToolBar *self) {
  self->clear();
}

//  QAction *QToolBar::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar12addSeparatorEv(QToolBar *self) {
  return self->addSeparator();
}

//  QAction *QToolBar::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar15insertSeparatorEP7QAction(
    QToolBar *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QToolBar::addWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar9addWidgetEP7QWidget(
    QToolBar *self,
    QWidget *widget) {
  return self->addWidget(widget);
}

//  QAction *QToolBar::insertWidget(QAction *before, QWidget *widget)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar12insertWidgetEP7QActionP7QWidget(
    QToolBar *self,
    QAction *before,
    QWidget *widget) {
  return self->insertWidget(before, widget);
}

//  QRect QToolBar::actionGeometry(QAction *action) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QToolBar14actionGeometryEP7QAction(
    const QToolBar *self,
    QAction *action) {
  return new QRect(self->actionGeometry(action));
}

//  QAction *QToolBar::actionAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar8actionAtERK6QPoint(
    const QToolBar *self,
    const QPoint *p) {
  return self->actionAt(*p);
}

//  QAction *QToolBar::actionAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar8actionAtEii(
    const QToolBar *self,
    int x,
    int y) {
  return self->actionAt(x, y);
}

//  QAction *QToolBar::toggleViewAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar16toggleViewActionEv(const QToolBar *self) {
  return self->toggleViewAction();
}

//  QSize QToolBar::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QToolBar8iconSizeEv(const QToolBar *self) {
  return new QSize(self->iconSize());
}

//  Qt::ToolButtonStyle QToolBar::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK8QToolBar15toolButtonStyleEv(
    const QToolBar *self) {
  return self->toolButtonStyle();
}

//  QWidget *QToolBar::widgetForAction(QAction *action) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBar15widgetForActionEP7QAction(
    const QToolBar *self,
    QAction *action) {
  return self->widgetForAction(action);
}

//  bool QToolBar::isFloatable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar11isFloatableEv(const QToolBar *self) {
  return self->isFloatable();
}

//  void QToolBar::setFloatable(bool floatable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar12setFloatableEb(QToolBar *self, bool floatable) {
  self->setFloatable(floatable);
}

//  bool QToolBar::isFloating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar10isFloatingEv(const QToolBar *self) {
  return self->isFloating();
}

//  void QToolBar::setIconSize(const QSize &iconSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar11setIconSizeERK5QSize(
    QToolBar *self,
    const QSize *iconSize) {
  self->setIconSize(*iconSize);
}

//  void QToolBar::setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QToolBar *self,
    Qt::ToolButtonStyle toolButtonStyle) {
  self->setToolButtonStyle(toolButtonStyle);
}

//  void QToolBar::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar11actionEventEP12QActionEvent(
    QToolBar *self,
    QActionEvent *event) {
  self->actionEvent(event);
}

//  void QToolBar::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar11changeEventEP6QEvent(
    QToolBar *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QToolBar::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar10paintEventEP11QPaintEvent(
    QToolBar *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  bool QToolBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QToolBar5eventEP6QEvent(QToolBar *self, QEvent *event) {
  return self->event(event);
}

//  void QToolBar::initStyleOption(QStyleOptionToolBar *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar(
    const QToolBar *self,
    QStyleOptionToolBar *option) {
  self->initStyleOption(option);
}

//  QToolBarPrivate *QToolBar::d_func()
extern "C" Q_DECL_EXPORT
QToolBarPrivate *ritual_ZN8QToolBar6d_funcEv(QToolBar *self) {
  return self->d_func();
}

//  const QToolBarPrivate *QToolBar::d_func() const
extern "C" Q_DECL_EXPORT
const QToolBarPrivate *ritual_ZNK8QToolBar6d_funcEv(const QToolBar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQToolBar, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBar(QToolBar *self, const char *key, void *call) {
  return static_cast<CuteQToolBar *>(self)->take(key, call);
}

//  void QToolBar::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBar11actionEventEP12QActionEvent(
    QToolBar *self,
    QActionEvent *event) {
  static_cast<OwnQToolBar *>(self)->OwnQToolBar::actionEvent(event);
}

//  void QToolBar::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBar11changeEventEP6QEvent(
    QToolBar *self,
    QEvent *event) {
  static_cast<OwnQToolBar *>(self)->OwnQToolBar::changeEvent(event);
}

//  void QToolBar::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QToolBar10paintEventEP11QPaintEvent(
    QToolBar *self,
    QPaintEvent *event) {
  static_cast<OwnQToolBar *>(self)->OwnQToolBar::paintEvent(event);
}

//  bool QToolBar::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QToolBar5eventEP6QEvent(QToolBar *self, QEvent *event) {
  return static_cast<OwnQToolBar *>(self)->OwnQToolBar::event(event);
}

//  void QToolBar::initStyleOption(QStyleOptionToolBar *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar(
    const QToolBar *self,
    QStyleOptionToolBar *option) {
  static_cast<const OwnQToolBar *>(self)->OwnQToolBar::initStyleOption(
      option);
}

//  QList<QToolBar *>::QList()
extern "C" Q_DECL_EXPORT
QList<QToolBar *> *ritual_list_make_QToolBar_ptr() {
  return new QList<QToolBar *>();
}

//  void QList<QToolBar *>::append(const QToolBar * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QToolBar_ptr(
    QList<QToolBar *> *self,
    QToolBar *element) {
  self->append(element);
}

//  qsizetype QList<QToolBar *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QToolBar_ptr(const QList<QToolBar *> *self) {
  return self->size();
}

//  const QToolBar * &QList<QToolBar *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QToolBar *ritual_list_at_QToolBar_ptr(
    const QList<QToolBar *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QToolBar *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QToolBar_ptr(QList<QToolBar *> *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
