//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dockwidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_dockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerDockWidget that Python can take functions over in. Every QDesignerDockWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDesignerDockWidgetCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDesignerDockWidgetCall1)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDesignerDockWidgetCall2)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(dockwidget)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dockwidget)
typedef bool (*CuteQDesignerDockWidgetCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dockwidget)
typedef void (*CuteQDesignerDockWidgetCall4)(const void *, QStyleOptionDockWidget *, int *);
#endif  // QT_CONFIG(dockwidget)
typedef int (*CuteQDesignerDockWidgetCall5)(const void *, int *);
typedef void (*CuteQDesignerDockWidgetCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerDockWidgetCall7)(const void *, int *);
typedef const QSize * (*CuteQDesignerDockWidgetCall8)(const void *, int *);
typedef int (*CuteQDesignerDockWidgetCall9)(const void *, int, int *);
typedef bool (*CuteQDesignerDockWidgetCall10)(const void *, int *);
typedef void * (*CuteQDesignerDockWidgetCall11)(const void *, int *);
typedef void (*CuteQDesignerDockWidgetCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall15)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerDockWidgetCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerDockWidgetCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall21)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall22)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall24)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerDockWidgetCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerDockWidgetCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerDockWidgetCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerDockWidgetCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerDockWidgetCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerDockWidgetCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerDockWidgetCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerDockWidgetCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerDockWidgetCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQDesignerDockWidgetCall34)(const void *, int, int *);
typedef void (*CuteQDesignerDockWidgetCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerDockWidgetCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerDockWidgetCall37)(const void *, int *);
typedef void (*CuteQDesignerDockWidgetCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerDockWidgetCall39)(const void *, int, int *);
typedef bool (*CuteQDesignerDockWidgetCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerDockWidgetCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerDockWidgetCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerDockWidgetCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerDockWidgetCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerDockWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerDockWidgetCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerDockWidget : public QDesignerDockWidget {
public:
  using QDesignerDockWidget::QDesignerDockWidget;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDockWidget")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
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

#if QT_CONFIG(dockwidget)
  //  void QDockWidget::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall0 call = reinterpret_cast<CuteQDesignerDockWidgetCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::changeEvent(event);
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  void QDockWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall1 call = reinterpret_cast<CuteQDesignerDockWidgetCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::closeEvent(event);
  }
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
  //  void QDockWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall2 call = reinterpret_cast<CuteQDesignerDockWidgetCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDockWidget::paintEvent(event);
  }
#endif  // QT_CONFIG(dockwidget)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dockwidget)
  //  bool QDockWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall3 call = reinterpret_cast<CuteQDesignerDockWidgetCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QDockWidget::event(event);
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(dockwidget)
  //  void QDockWidget::initStyleOption(QStyleOptionDockWidget *option)
  //      const
  void initStyleOption(QStyleOptionDockWidget *option) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall4 call = reinterpret_cast<CuteQDesignerDockWidgetCall4>(taken[4]);
      call(this, option, &handled);
      if (handled) return;
    }
    QDockWidget::initStyleOption(option);
  }
#endif  // QT_CONFIG(dockwidget)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall5 call = reinterpret_cast<CuteQDesignerDockWidgetCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall6 call = reinterpret_cast<CuteQDesignerDockWidgetCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall7 call = reinterpret_cast<CuteQDesignerDockWidgetCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall8 call = reinterpret_cast<CuteQDesignerDockWidgetCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall9 call = reinterpret_cast<CuteQDesignerDockWidgetCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall10 call = reinterpret_cast<CuteQDesignerDockWidgetCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall11 call = reinterpret_cast<CuteQDesignerDockWidgetCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall12 call = reinterpret_cast<CuteQDesignerDockWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall13 call = reinterpret_cast<CuteQDesignerDockWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall14 call = reinterpret_cast<CuteQDesignerDockWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall15 call = reinterpret_cast<CuteQDesignerDockWidgetCall15>(taken[15]);
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
      CuteQDesignerDockWidgetCall16 call = reinterpret_cast<CuteQDesignerDockWidgetCall16>(taken[16]);
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
      CuteQDesignerDockWidgetCall17 call = reinterpret_cast<CuteQDesignerDockWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall18 call = reinterpret_cast<CuteQDesignerDockWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall19 call = reinterpret_cast<CuteQDesignerDockWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall20 call = reinterpret_cast<CuteQDesignerDockWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall21 call = reinterpret_cast<CuteQDesignerDockWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall22 call = reinterpret_cast<CuteQDesignerDockWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall23 call = reinterpret_cast<CuteQDesignerDockWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall24 call = reinterpret_cast<CuteQDesignerDockWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall25 call = reinterpret_cast<CuteQDesignerDockWidgetCall25>(taken[25]);
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
      CuteQDesignerDockWidgetCall26 call = reinterpret_cast<CuteQDesignerDockWidgetCall26>(taken[26]);
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
      CuteQDesignerDockWidgetCall27 call = reinterpret_cast<CuteQDesignerDockWidgetCall27>(taken[27]);
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
      CuteQDesignerDockWidgetCall28 call = reinterpret_cast<CuteQDesignerDockWidgetCall28>(taken[28]);
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
      CuteQDesignerDockWidgetCall29 call = reinterpret_cast<CuteQDesignerDockWidgetCall29>(taken[29]);
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
      CuteQDesignerDockWidgetCall30 call = reinterpret_cast<CuteQDesignerDockWidgetCall30>(taken[30]);
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
      CuteQDesignerDockWidgetCall31 call = reinterpret_cast<CuteQDesignerDockWidgetCall31>(taken[31]);
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
      CuteQDesignerDockWidgetCall32 call = reinterpret_cast<CuteQDesignerDockWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall33 call = reinterpret_cast<CuteQDesignerDockWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall34 call = reinterpret_cast<CuteQDesignerDockWidgetCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall35 call = reinterpret_cast<CuteQDesignerDockWidgetCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall36 call = reinterpret_cast<CuteQDesignerDockWidgetCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall37 call = reinterpret_cast<CuteQDesignerDockWidgetCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall38 call = reinterpret_cast<CuteQDesignerDockWidgetCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall39 call = reinterpret_cast<CuteQDesignerDockWidgetCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerDockWidgetCall40 call = reinterpret_cast<CuteQDesignerDockWidgetCall40>(taken[40]);
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
      CuteQDesignerDockWidgetCall41 call = reinterpret_cast<CuteQDesignerDockWidgetCall41>(taken[41]);
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
      CuteQDesignerDockWidgetCall42 call = reinterpret_cast<CuteQDesignerDockWidgetCall42>(taken[42]);
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
      CuteQDesignerDockWidgetCall43 call = reinterpret_cast<CuteQDesignerDockWidgetCall43>(taken[43]);
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
      CuteQDesignerDockWidgetCall44 call = reinterpret_cast<CuteQDesignerDockWidgetCall44>(taken[44]);
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
      CuteQDesignerDockWidgetCall45 call = reinterpret_cast<CuteQDesignerDockWidgetCall45>(taken[45]);
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
      CuteQDesignerDockWidgetCall46 call = reinterpret_cast<CuteQDesignerDockWidgetCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerDockWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QDesignerDockWidget10metaObjectEv(
    const QDesignerDockWidget *self) {
  return self->metaObject();
}

//  void *QDesignerDockWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QDesignerDockWidget11qt_metacastEPKc(
    QDesignerDockWidget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerDockWidget::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QDesignerDockWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerDockWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerDockWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QDesignerDockWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerDockWidget::tr(s, c, n));
}

//  QDesignerDockWidget::QDesignerDockWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerDockWidget *ritual_ZN19QDesignerDockWidgetC1EP7QWidget(
    QWidget *parent) {
  return new CuteQDesignerDockWidget(parent);
}

//  QDesignerDockWidget::~QDesignerDockWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDesignerDockWidgetD1Ev(QDesignerDockWidget *self) {
  delete self;
}

//  bool QDesignerDockWidget::docked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDesignerDockWidget6dockedEv(
    const QDesignerDockWidget *self) {
  return self->docked();
}

//  void QDesignerDockWidget::setDocked(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDesignerDockWidget9setDockedEb(
    QDesignerDockWidget *self,
    bool b) {
  self->setDocked(b);
}

//  Qt::DockWidgetArea QDesignerDockWidget::dockWidgetArea() const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK19QDesignerDockWidget14dockWidgetAreaEv(
    const QDesignerDockWidget *self) {
  return self->dockWidgetArea();
}

//  void QDesignerDockWidget::setDockWidgetArea(Qt::DockWidgetArea
//      dockWidgetArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDesignerDockWidget17setDockWidgetAreaEN2Qt14DockWidgetAreaE(
    QDesignerDockWidget *self,
    Qt::DockWidgetArea dockWidgetArea) {
  self->setDockWidgetArea(dockWidgetArea);
}

//  bool QDesignerDockWidget::inMainWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDesignerDockWidget12inMainWindowEv(
    const QDesignerDockWidget *self) {
  return self->inMainWindow();
}

//  QDesignerFormWindowInterface *QDesignerDockWidget::formWindow() const
extern "C" Q_DECL_EXPORT
QDesignerFormWindowInterface *ritual_ZNK19QDesignerDockWidget10formWindowEv(
    const QDesignerDockWidget *self) {
  return self->formWindow();
}

//  QMainWindow *QDesignerDockWidget::findMainWindow() const
extern "C" Q_DECL_EXPORT
QMainWindow *ritual_ZNK19QDesignerDockWidget14findMainWindowEv(
    const QDesignerDockWidget *self) {
  return self->findMainWindow();
}

//  a Python function taken by a CuteQDesignerDockWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerDockWidget(
    QDesignerDockWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerDockWidget *>(self)->take(key, call);
}
