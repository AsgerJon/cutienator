//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qregion.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfontinfo.h>
#include <QtGui/qcursor.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qicon.h>
#include <QtCore/qlocale.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qbytearray.h>
#include <QtWidgets/qsizepolicy.h>
#include <QtCore/qmargins.h>
#include <QtGui/qaction.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWidget : QWidget {
  using QWidget::event;
  using QWidget::mousePressEvent;
  using QWidget::mouseReleaseEvent;
  using QWidget::mouseDoubleClickEvent;
  using QWidget::mouseMoveEvent;
  using QWidget::wheelEvent;
  using QWidget::keyPressEvent;
  using QWidget::keyReleaseEvent;
  using QWidget::focusInEvent;
  using QWidget::focusOutEvent;
  using QWidget::enterEvent;
  using QWidget::leaveEvent;
  using QWidget::paintEvent;
  using QWidget::moveEvent;
  using QWidget::resizeEvent;
  using QWidget::closeEvent;
  using QWidget::contextMenuEvent;
  using QWidget::tabletEvent;
  using QWidget::actionEvent;
  using QWidget::dragEnterEvent;
  using QWidget::dragMoveEvent;
  using QWidget::dragLeaveEvent;
  using QWidget::dropEvent;
  using QWidget::showEvent;
  using QWidget::hideEvent;
  using QWidget::changeEvent;
  using QWidget::metric;
  using QWidget::initPainter;
  using QWidget::redirected;
  using QWidget::sharedPainter;
  using QWidget::inputMethodEvent;
  using QWidget::focusNextPrevChild;
};

//  A QWidget that Python can take functions over in. Every QWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQWidgetCall0)(const void *, int *);
typedef void (*CuteQWidgetCall1)(const void *, bool, int *);
typedef const QSize * (*CuteQWidgetCall2)(const void *, int *);
typedef const QSize * (*CuteQWidgetCall3)(const void *, int *);
typedef int (*CuteQWidgetCall4)(const void *, int, int *);
typedef bool (*CuteQWidgetCall5)(const void *, int *);
typedef void * (*CuteQWidgetCall6)(const void *, int *);
typedef bool (*CuteQWidgetCall7)(const void *, QEvent *, int *);
typedef void (*CuteQWidgetCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetCall12)(const void *, QWheelEvent *, int *);
typedef void (*CuteQWidgetCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWidgetCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWidgetCall17)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWidgetCall18)(const void *, QEvent *, int *);
typedef void (*CuteQWidgetCall19)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWidgetCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWidgetCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWidgetCall22)(const void *, QCloseEvent *, int *);
typedef void (*CuteQWidgetCall23)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQWidgetCall24)(const void *, QTabletEvent *, int *);
typedef void (*CuteQWidgetCall25)(const void *, QActionEvent *, int *);
typedef void (*CuteQWidgetCall26)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQWidgetCall27)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQWidgetCall28)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQWidgetCall29)(const void *, QDropEvent *, int *);
typedef void (*CuteQWidgetCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQWidgetCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQWidgetCall32)(const void *, QEvent *, int *);
typedef int (*CuteQWidgetCall33)(const void *, int, int *);
typedef void (*CuteQWidgetCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQWidgetCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQWidgetCall36)(const void *, int *);
typedef void (*CuteQWidgetCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWidgetCall38)(const void *, int, int *);
typedef bool (*CuteQWidgetCall39)(const void *, bool, int *);
typedef bool (*CuteQWidgetCall40)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWidgetCall41)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWidgetCall42)(const void *, QChildEvent *, int *);
typedef void (*CuteQWidgetCall43)(const void *, QEvent *, int *);
typedef void (*CuteQWidgetCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWidgetCall45)(const void *, const QMetaMethod *, int *);
class CuteQWidget : public QWidget {
public:
  using QWidget::QWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    return false;
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetCall0 call = reinterpret_cast<CuteQWidgetCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetCall1 call = reinterpret_cast<CuteQWidgetCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetCall2 call = reinterpret_cast<CuteQWidgetCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetCall3 call = reinterpret_cast<CuteQWidgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetCall4 call = reinterpret_cast<CuteQWidgetCall4>(taken[4]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetCall5 call = reinterpret_cast<CuteQWidgetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetCall6 call = reinterpret_cast<CuteQWidgetCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetCall7 call = reinterpret_cast<CuteQWidgetCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetCall8 call = reinterpret_cast<CuteQWidgetCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetCall9 call = reinterpret_cast<CuteQWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetCall10 call = reinterpret_cast<CuteQWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWidgetCall11 call = reinterpret_cast<CuteQWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWidgetCall12 call = reinterpret_cast<CuteQWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWidgetCall13 call = reinterpret_cast<CuteQWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWidgetCall14 call = reinterpret_cast<CuteQWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWidgetCall15 call = reinterpret_cast<CuteQWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWidgetCall16 call = reinterpret_cast<CuteQWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWidgetCall17 call = reinterpret_cast<CuteQWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWidgetCall18 call = reinterpret_cast<CuteQWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWidgetCall19 call = reinterpret_cast<CuteQWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWidgetCall20 call = reinterpret_cast<CuteQWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWidgetCall21 call = reinterpret_cast<CuteQWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWidgetCall22 call = reinterpret_cast<CuteQWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWidgetCall23 call = reinterpret_cast<CuteQWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWidgetCall24 call = reinterpret_cast<CuteQWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWidgetCall25 call = reinterpret_cast<CuteQWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWidgetCall26 call = reinterpret_cast<CuteQWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWidgetCall27 call = reinterpret_cast<CuteQWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWidgetCall28 call = reinterpret_cast<CuteQWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWidgetCall29 call = reinterpret_cast<CuteQWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWidgetCall30 call = reinterpret_cast<CuteQWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWidgetCall31 call = reinterpret_cast<CuteQWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWidgetCall32 call = reinterpret_cast<CuteQWidgetCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQWidgetCall33 call = reinterpret_cast<CuteQWidgetCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQWidgetCall34 call = reinterpret_cast<CuteQWidgetCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQWidgetCall35 call = reinterpret_cast<CuteQWidgetCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQWidgetCall36 call = reinterpret_cast<CuteQWidgetCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQWidgetCall37 call = reinterpret_cast<CuteQWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQWidgetCall38 call = reinterpret_cast<CuteQWidgetCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQWidgetCall39 call = reinterpret_cast<CuteQWidgetCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWidgetCall40 call = reinterpret_cast<CuteQWidgetCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQWidgetCall41 call = reinterpret_cast<CuteQWidgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQWidgetCall42 call = reinterpret_cast<CuteQWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQWidgetCall43 call = reinterpret_cast<CuteQWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQWidgetCall44 call = reinterpret_cast<CuteQWidgetCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQWidgetCall45 call = reinterpret_cast<CuteQWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QWidget10metaObjectEv(const QWidget *self) {
  return self->metaObject();
}

//  QString QWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QWidget2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWidget::tr(s, c, n));
}

//  QWidgetPrivate *QWidget::d_func()
extern "C" Q_DECL_EXPORT
QWidgetPrivate *ritual_ZN7QWidget6d_funcEv(QWidget *self) {
  return self->d_func();
}

//  const QWidgetPrivate *QWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QWidgetPrivate *ritual_ZNK7QWidget6d_funcEv(const QWidget *self) {
  return self->d_func();
}

//  QWidget::QWidget(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN7QWidgetC1EPS_6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQWidget(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QWidget::~QWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidgetD1Ev(QWidget *self) {
  delete self;
}

//  int QWidget::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget7devTypeEv(const QWidget *self) {
  return self->devType();
}

//  WId QWidget::winId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK7QWidget5winIdEv(const QWidget *self) {
  return self->winId();
}

//  void QWidget::createWinId()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11createWinIdEv(QWidget *self) {
  self->createWinId();
}

//  WId QWidget::internalWinId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK7QWidget13internalWinIdEv(const QWidget *self) {
  return self->internalWinId();
}

//  WId QWidget::effectiveWinId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK7QWidget14effectiveWinIdEv(const QWidget *self) {
  return self->effectiveWinId();
}

//  QStyle *QWidget::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK7QWidget5styleEv(const QWidget *self) {
  return self->style();
}

//  void QWidget::setStyle(QStyle *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget8setStyleEP6QStyle(QWidget *self, QStyle *a0) {
  self->setStyle(a0);
}

//  bool QWidget::isTopLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget10isTopLevelEv(const QWidget *self) {
  return self->isTopLevel();
}

//  bool QWidget::isWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget8isWindowEv(const QWidget *self) {
  return self->isWindow();
}

//  bool QWidget::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget7isModalEv(const QWidget *self) {
  return self->isModal();
}

//  Qt::WindowModality QWidget::windowModality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK7QWidget14windowModalityEv(
    const QWidget *self) {
  return self->windowModality();
}

//  void QWidget::setWindowModality(Qt::WindowModality windowModality)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setWindowModalityEN2Qt14WindowModalityE(
    QWidget *self,
    Qt::WindowModality windowModality) {
  self->setWindowModality(windowModality);
}

//  bool QWidget::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget9isEnabledEv(const QWidget *self) {
  return self->isEnabled();
}

//  bool QWidget::isEnabledTo(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget11isEnabledToEPKS_(
    const QWidget *self,
    const QWidget *a0) {
  return self->isEnabledTo(a0);
}

//  void QWidget::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10setEnabledEb(QWidget *self, bool a0) {
  self->setEnabled(a0);
}

//  void QWidget::setDisabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setDisabledEb(QWidget *self, bool a0) {
  self->setDisabled(a0);
}

//  void QWidget::setWindowModified(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setWindowModifiedEb(QWidget *self, bool a0) {
  self->setWindowModified(a0);
}

//  QRect QWidget::frameGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget13frameGeometryEv(const QWidget *self) {
  return new QRect(self->frameGeometry());
}

//  const QRect &QWidget::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget8geometryEv(const QWidget *self) {
  return new QRect(self->geometry());
}

//  QRect QWidget::normalGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget14normalGeometryEv(const QWidget *self) {
  return new QRect(self->normalGeometry());
}

//  int QWidget::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget1xEv(const QWidget *self) {
  return self->x();
}

//  int QWidget::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget1yEv(const QWidget *self) {
  return self->y();
}

//  QPoint QWidget::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget3posEv(const QWidget *self) {
  return new QPoint(self->pos());
}

//  QSize QWidget::frameSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget9frameSizeEv(const QWidget *self) {
  return new QSize(self->frameSize());
}

//  QSize QWidget::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget4sizeEv(const QWidget *self) {
  return new QSize(self->size());
}

//  int QWidget::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget5widthEv(const QWidget *self) {
  return self->width();
}

//  int QWidget::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget6heightEv(const QWidget *self) {
  return self->height();
}

//  QRect QWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget4rectEv(const QWidget *self) {
  return new QRect(self->rect());
}

//  QRect QWidget::childrenRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget12childrenRectEv(const QWidget *self) {
  return new QRect(self->childrenRect());
}

//  QRegion QWidget::childrenRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QWidget14childrenRegionEv(const QWidget *self) {
  return new QRegion(self->childrenRegion());
}

//  QSize QWidget::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget11minimumSizeEv(const QWidget *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWidget::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget11maximumSizeEv(const QWidget *self) {
  return new QSize(self->maximumSize());
}

//  int QWidget::minimumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget12minimumWidthEv(const QWidget *self) {
  return self->minimumWidth();
}

//  int QWidget::minimumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget13minimumHeightEv(const QWidget *self) {
  return self->minimumHeight();
}

//  int QWidget::maximumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget12maximumWidthEv(const QWidget *self) {
  return self->maximumWidth();
}

//  int QWidget::maximumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget13maximumHeightEv(const QWidget *self) {
  return self->maximumHeight();
}

//  void QWidget::setMinimumSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setMinimumSizeERK5QSize(
    QWidget *self,
    const QSize *a0) {
  self->setMinimumSize(*a0);
}

//  void QWidget::setMinimumSize(int minw, int minh)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setMinimumSizeEii(
    QWidget *self,
    int minw,
    int minh) {
  self->setMinimumSize(minw, minh);
}

//  void QWidget::setMaximumSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setMaximumSizeERK5QSize(
    QWidget *self,
    const QSize *a0) {
  self->setMaximumSize(*a0);
}

//  void QWidget::setMaximumSize(int maxw, int maxh)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setMaximumSizeEii(
    QWidget *self,
    int maxw,
    int maxh) {
  self->setMaximumSize(maxw, maxh);
}

//  void QWidget::setMinimumWidth(int minw)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15setMinimumWidthEi(QWidget *self, int minw) {
  self->setMinimumWidth(minw);
}

//  void QWidget::setMinimumHeight(int minh)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setMinimumHeightEi(QWidget *self, int minh) {
  self->setMinimumHeight(minh);
}

//  void QWidget::setMaximumWidth(int maxw)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15setMaximumWidthEi(QWidget *self, int maxw) {
  self->setMaximumWidth(maxw);
}

//  void QWidget::setMaximumHeight(int maxh)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setMaximumHeightEi(QWidget *self, int maxh) {
  self->setMaximumHeight(maxh);
}

//  QSize QWidget::sizeIncrement() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget13sizeIncrementEv(const QWidget *self) {
  return new QSize(self->sizeIncrement());
}

//  void QWidget::setSizeIncrement(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setSizeIncrementERK5QSize(
    QWidget *self,
    const QSize *a0) {
  self->setSizeIncrement(*a0);
}

//  void QWidget::setSizeIncrement(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setSizeIncrementEii(QWidget *self, int w, int h) {
  self->setSizeIncrement(w, h);
}

//  QSize QWidget::baseSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget8baseSizeEv(const QWidget *self) {
  return new QSize(self->baseSize());
}

//  void QWidget::setBaseSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setBaseSizeERK5QSize(
    QWidget *self,
    const QSize *a0) {
  self->setBaseSize(*a0);
}

//  void QWidget::setBaseSize(int basew, int baseh)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setBaseSizeEii(QWidget *self, int basew, int baseh) {
  self->setBaseSize(basew, baseh);
}

//  void QWidget::setFixedSize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12setFixedSizeERK5QSize(
    QWidget *self,
    const QSize *a0) {
  self->setFixedSize(*a0);
}

//  void QWidget::setFixedSize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12setFixedSizeEii(QWidget *self, int w, int h) {
  self->setFixedSize(w, h);
}

//  void QWidget::setFixedWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setFixedWidthEi(QWidget *self, int w) {
  self->setFixedWidth(w);
}

//  void QWidget::setFixedHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setFixedHeightEi(QWidget *self, int h) {
  self->setFixedHeight(h);
}

//  QPointF QWidget::mapToGlobal(const QPointF &a0) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget11mapToGlobalERK7QPointF(
    const QWidget *self,
    const QPointF *a0) {
  return new QPointF(self->mapToGlobal(*a0));
}

//  QPoint QWidget::mapToGlobal(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget11mapToGlobalERK6QPoint(
    const QWidget *self,
    const QPoint *a0) {
  return new QPoint(self->mapToGlobal(*a0));
}

//  QPointF QWidget::mapFromGlobal(const QPointF &a0) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget13mapFromGlobalERK7QPointF(
    const QWidget *self,
    const QPointF *a0) {
  return new QPointF(self->mapFromGlobal(*a0));
}

//  QPoint QWidget::mapFromGlobal(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget13mapFromGlobalERK6QPoint(
    const QWidget *self,
    const QPoint *a0) {
  return new QPoint(self->mapFromGlobal(*a0));
}

//  QPointF QWidget::mapToParent(const QPointF &a0) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget11mapToParentERK7QPointF(
    const QWidget *self,
    const QPointF *a0) {
  return new QPointF(self->mapToParent(*a0));
}

//  QPoint QWidget::mapToParent(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget11mapToParentERK6QPoint(
    const QWidget *self,
    const QPoint *a0) {
  return new QPoint(self->mapToParent(*a0));
}

//  QPointF QWidget::mapFromParent(const QPointF &a0) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget13mapFromParentERK7QPointF(
    const QWidget *self,
    const QPointF *a0) {
  return new QPointF(self->mapFromParent(*a0));
}

//  QPoint QWidget::mapFromParent(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget13mapFromParentERK6QPoint(
    const QWidget *self,
    const QPoint *a0) {
  return new QPoint(self->mapFromParent(*a0));
}

//  QPointF QWidget::mapTo(const QWidget *a0, const QPointF &a1) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget5mapToEPKS_RK7QPointF(
    const QWidget *self,
    const QWidget *a0,
    const QPointF *a1) {
  return new QPointF(self->mapTo(a0, *a1));
}

//  QPoint QWidget::mapTo(const QWidget *a0, const QPoint &a1) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget5mapToEPKS_RK6QPoint(
    const QWidget *self,
    const QWidget *a0,
    const QPoint *a1) {
  return new QPoint(self->mapTo(a0, *a1));
}

//  QPointF QWidget::mapFrom(const QWidget *a0, const QPointF &a1) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWidget7mapFromEPKS_RK7QPointF(
    const QWidget *self,
    const QWidget *a0,
    const QPointF *a1) {
  return new QPointF(self->mapFrom(a0, *a1));
}

//  QPoint QWidget::mapFrom(const QWidget *a0, const QPoint &a1) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWidget7mapFromEPKS_RK6QPoint(
    const QWidget *self,
    const QWidget *a0,
    const QPoint *a1) {
  return new QPoint(self->mapFrom(a0, *a1));
}

//  QWidget *QWidget::window() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget6windowEv(const QWidget *self) {
  return self->window();
}

//  QWidget *QWidget::nativeParentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget18nativeParentWidgetEv(const QWidget *self) {
  return self->nativeParentWidget();
}

//  QWidget *QWidget::topLevelWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget14topLevelWidgetEv(const QWidget *self) {
  return self->topLevelWidget();
}

//  const QPalette &QWidget::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK7QWidget7paletteEv(const QWidget *self) {
  return new QPalette(self->palette());
}

//  void QWidget::setPalette(const QPalette &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10setPaletteERK8QPalette(
    QWidget *self,
    const QPalette *a0) {
  self->setPalette(*a0);
}

//  void QWidget::setBackgroundRole(QPalette::ColorRole a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setBackgroundRoleEN8QPalette9ColorRoleE(
    QWidget *self,
    QPalette::ColorRole a0) {
  self->setBackgroundRole(a0);
}

//  QPalette::ColorRole QWidget::backgroundRole() const
extern "C" Q_DECL_EXPORT
QPalette::ColorRole ritual_ZNK7QWidget14backgroundRoleEv(
    const QWidget *self) {
  return self->backgroundRole();
}

//  void QWidget::setForegroundRole(QPalette::ColorRole a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setForegroundRoleEN8QPalette9ColorRoleE(
    QWidget *self,
    QPalette::ColorRole a0) {
  self->setForegroundRole(a0);
}

//  QPalette::ColorRole QWidget::foregroundRole() const
extern "C" Q_DECL_EXPORT
QPalette::ColorRole ritual_ZNK7QWidget14foregroundRoleEv(
    const QWidget *self) {
  return self->foregroundRole();
}

//  const QFont &QWidget::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK7QWidget4fontEv(const QWidget *self) {
  return new QFont(self->font());
}

//  void QWidget::setFont(const QFont &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7setFontERK5QFont(QWidget *self, const QFont *a0) {
  self->setFont(*a0);
}

//  QFontMetrics QWidget::fontMetrics() const
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZNK7QWidget11fontMetricsEv(const QWidget *self) {
  return new QFontMetrics(self->fontMetrics());
}

//  QFontInfo QWidget::fontInfo() const
extern "C" Q_DECL_EXPORT
QFontInfo *ritual_ZNK7QWidget8fontInfoEv(const QWidget *self) {
  return new QFontInfo(self->fontInfo());
}

//  QCursor QWidget::cursor() const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK7QWidget6cursorEv(const QWidget *self) {
  return new QCursor(self->cursor());
}

//  void QWidget::setCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setCursorERK7QCursor(
    QWidget *self,
    const QCursor *a0) {
  self->setCursor(*a0);
}

//  void QWidget::unsetCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11unsetCursorEv(QWidget *self) {
  self->unsetCursor();
}

//  void QWidget::setMouseTracking(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setMouseTrackingEb(QWidget *self, bool enable) {
  self->setMouseTracking(enable);
}

//  bool QWidget::hasMouseTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget16hasMouseTrackingEv(const QWidget *self) {
  return self->hasMouseTracking();
}

//  bool QWidget::underMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget10underMouseEv(const QWidget *self) {
  return self->underMouse();
}

//  void QWidget::setTabletTracking(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setTabletTrackingEb(QWidget *self, bool enable) {
  self->setTabletTracking(enable);
}

//  bool QWidget::hasTabletTracking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget17hasTabletTrackingEv(const QWidget *self) {
  return self->hasTabletTracking();
}

//  void QWidget::setMask(const QBitmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7setMaskERK7QBitmap(QWidget *self, const QBitmap *a0) {
  self->setMask(*a0);
}

//  void QWidget::setMask(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7setMaskERK7QRegion(QWidget *self, const QRegion *a0) {
  self->setMask(*a0);
}

//  QRegion QWidget::mask() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QWidget4maskEv(const QWidget *self) {
  return new QRegion(self->mask());
}

//  void QWidget::clearMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9clearMaskEv(QWidget *self) {
  self->clearMask();
}

//  void QWidget::render(QPaintDevice *target, const QPoint &targetOffset,
//      const QRegion &sourceRegion, RenderFlags renderFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6renderEP12QPaintDeviceRK6QPointRK7QRegion6QFlagsINS_10RenderFlagEE(
    QWidget *self,
    QPaintDevice *target,
    const QPoint *targetOffset,
    const QRegion *sourceRegion,
    int renderFlags) {
  self->render(
      target,
      *targetOffset,
      *sourceRegion,
      QFlags<QWidget::RenderFlag>::fromInt(renderFlags));
}

//  void QWidget::render(QPainter *painter, const QPoint &targetOffset, const
//      QRegion &sourceRegion, RenderFlags renderFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6renderEP8QPainterRK6QPointRK7QRegion6QFlagsINS_10RenderFlagEE(
    QWidget *self,
    QPainter *painter,
    const QPoint *targetOffset,
    const QRegion *sourceRegion,
    int renderFlags) {
  self->render(
      painter,
      *targetOffset,
      *sourceRegion,
      QFlags<QWidget::RenderFlag>::fromInt(renderFlags));
}

//  QPixmap QWidget::grab(const QRect &rectangle)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN7QWidget4grabERK5QRect(
    QWidget *self,
    const QRect *rectangle) {
  return new QPixmap(self->grab(*rectangle));
}

//  QGraphicsEffect *QWidget::graphicsEffect() const
extern "C" Q_DECL_EXPORT
QGraphicsEffect *ritual_ZNK7QWidget14graphicsEffectEv(const QWidget *self) {
  return self->graphicsEffect();
}

//  void QWidget::setGraphicsEffect(QGraphicsEffect *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setGraphicsEffectEP15QGraphicsEffect(
    QWidget *self,
    QGraphicsEffect *effect) {
  self->setGraphicsEffect(effect);
}

//  void QWidget::grabGesture(Qt::GestureType type, Qt::GestureFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11grabGestureEN2Qt11GestureTypeE6QFlagsINS0_11GestureFlagEE(
    QWidget *self,
    Qt::GestureType type,
    int flags) {
  self->grabGesture(type, QFlags<Qt::GestureFlag>::fromInt(flags));
}

//  void QWidget::ungrabGesture(Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13ungrabGestureEN2Qt11GestureTypeE(
    QWidget *self,
    Qt::GestureType type) {
  self->ungrabGesture(type);
}

//  void QWidget::setWindowTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setWindowTitleERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setWindowTitle(*a0);
}

//  void QWidget::setStyleSheet(const QString &styleSheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setStyleSheetERK7QString(
    QWidget *self,
    const QString *styleSheet) {
  self->setStyleSheet(*styleSheet);
}

//  QString QWidget::styleSheet() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget10styleSheetEv(const QWidget *self) {
  return new QString(self->styleSheet());
}

//  QString QWidget::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget11windowTitleEv(const QWidget *self) {
  return new QString(self->windowTitle());
}

//  void QWidget::setWindowIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setWindowIconERK5QIcon(
    QWidget *self,
    const QIcon *icon) {
  self->setWindowIcon(*icon);
}

//  QIcon QWidget::windowIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QWidget10windowIconEv(const QWidget *self) {
  return new QIcon(self->windowIcon());
}

//  void QWidget::setWindowIconText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setWindowIconTextERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setWindowIconText(*a0);
}

//  QString QWidget::windowIconText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget14windowIconTextEv(const QWidget *self) {
  return new QString(self->windowIconText());
}

//  void QWidget::setWindowRole(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setWindowRoleERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setWindowRole(*a0);
}

//  QString QWidget::windowRole() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget10windowRoleEv(const QWidget *self) {
  return new QString(self->windowRole());
}

//  void QWidget::setWindowFilePath(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setWindowFilePathERK7QString(
    QWidget *self,
    const QString *filePath) {
  self->setWindowFilePath(*filePath);
}

//  QString QWidget::windowFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget14windowFilePathEv(const QWidget *self) {
  return new QString(self->windowFilePath());
}

//  void QWidget::setWindowOpacity(qreal level)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16setWindowOpacityEd(QWidget *self, qreal level) {
  self->setWindowOpacity(level);
}

//  qreal QWidget::windowOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QWidget13windowOpacityEv(const QWidget *self) {
  return self->windowOpacity();
}

//  bool QWidget::isWindowModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget16isWindowModifiedEv(const QWidget *self) {
  return self->isWindowModified();
}

//  void QWidget::setToolTip(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10setToolTipERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setToolTip(*a0);
}

//  QString QWidget::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget7toolTipEv(const QWidget *self) {
  return new QString(self->toolTip());
}

//  void QWidget::setToolTipDuration(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget18setToolTipDurationEi(QWidget *self, int msec) {
  self->setToolTipDuration(msec);
}

//  int QWidget::toolTipDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget15toolTipDurationEv(const QWidget *self) {
  return self->toolTipDuration();
}

//  void QWidget::setStatusTip(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12setStatusTipERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setStatusTip(*a0);
}

//  QString QWidget::statusTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget9statusTipEv(const QWidget *self) {
  return new QString(self->statusTip());
}

//  void QWidget::setWhatsThis(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12setWhatsThisERK7QString(
    QWidget *self,
    const QString *a0) {
  self->setWhatsThis(*a0);
}

//  QString QWidget::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget9whatsThisEv(const QWidget *self) {
  return new QString(self->whatsThis());
}

//  QString QWidget::accessibleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget14accessibleNameEv(const QWidget *self) {
  return new QString(self->accessibleName());
}

//  void QWidget::setAccessibleName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setAccessibleNameERK7QString(
    QWidget *self,
    const QString *name) {
  self->setAccessibleName(*name);
}

//  QString QWidget::accessibleDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget21accessibleDescriptionEv(const QWidget *self) {
  return new QString(self->accessibleDescription());
}

//  void QWidget::setAccessibleDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget24setAccessibleDescriptionERK7QString(
    QWidget *self,
    const QString *description) {
  self->setAccessibleDescription(*description);
}

//  QString QWidget::accessibleIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWidget20accessibleIdentifierEv(const QWidget *self) {
  return new QString(self->accessibleIdentifier());
}

//  void QWidget::setAccessibleIdentifier(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget23setAccessibleIdentifierERK7QString(
    QWidget *self,
    const QString *identifier) {
  self->setAccessibleIdentifier(*identifier);
}

//  void QWidget::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QWidget *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  Qt::LayoutDirection QWidget::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK7QWidget15layoutDirectionEv(
    const QWidget *self) {
  return self->layoutDirection();
}

//  void QWidget::unsetLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget20unsetLayoutDirectionEv(QWidget *self) {
  self->unsetLayoutDirection();
}

//  void QWidget::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setLocaleERK7QLocale(
    QWidget *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QWidget::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK7QWidget6localeEv(const QWidget *self) {
  return new QLocale(self->locale());
}

//  void QWidget::unsetLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11unsetLocaleEv(QWidget *self) {
  self->unsetLocale();
}

//  bool QWidget::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget13isRightToLeftEv(const QWidget *self) {
  return self->isRightToLeft();
}

//  bool QWidget::isLeftToRight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget13isLeftToRightEv(const QWidget *self) {
  return self->isLeftToRight();
}

//  void QWidget::setFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget8setFocusEv(QWidget *self) {
  self->setFocus();
}

//  bool QWidget::isActiveWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget14isActiveWindowEv(const QWidget *self) {
  return self->isActiveWindow();
}

//  void QWidget::activateWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14activateWindowEv(QWidget *self) {
  self->activateWindow();
}

//  void QWidget::clearFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10clearFocusEv(QWidget *self) {
  self->clearFocus();
}

//  void QWidget::setFocus(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget8setFocusEN2Qt11FocusReasonE(
    QWidget *self,
    Qt::FocusReason reason) {
  self->setFocus(reason);
}

//  Qt::FocusPolicy QWidget::focusPolicy() const
extern "C" Q_DECL_EXPORT
Qt::FocusPolicy ritual_ZNK7QWidget11focusPolicyEv(const QWidget *self) {
  return self->focusPolicy();
}

//  void QWidget::setFocusPolicy(Qt::FocusPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setFocusPolicyEN2Qt11FocusPolicyE(
    QWidget *self,
    Qt::FocusPolicy policy) {
  self->setFocusPolicy(policy);
}

//  bool QWidget::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget8hasFocusEv(const QWidget *self) {
  return self->hasFocus();
}

//  void QWidget::setTabOrder(QWidget *a0, QWidget *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setTabOrderEPS_S0_(QWidget *a0, QWidget *a1) {
  QWidget::setTabOrder(a0, a1);
}

//  void QWidget::setFocusProxy(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setFocusProxyEPS_(QWidget *self, QWidget *a0) {
  self->setFocusProxy(a0);
}

//  QWidget *QWidget::focusProxy() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget10focusProxyEv(const QWidget *self) {
  return self->focusProxy();
}

//  Qt::ContextMenuPolicy QWidget::contextMenuPolicy() const
extern "C" Q_DECL_EXPORT
Qt::ContextMenuPolicy ritual_ZNK7QWidget17contextMenuPolicyEv(
    const QWidget *self) {
  return self->contextMenuPolicy();
}

//  void QWidget::setContextMenuPolicy(Qt::ContextMenuPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget20setContextMenuPolicyEN2Qt17ContextMenuPolicyE(
    QWidget *self,
    Qt::ContextMenuPolicy policy) {
  self->setContextMenuPolicy(policy);
}

//  void QWidget::grabMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9grabMouseEv(QWidget *self) {
  self->grabMouse();
}

//  void QWidget::grabMouse(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9grabMouseERK7QCursor(
    QWidget *self,
    const QCursor *a0) {
  self->grabMouse(*a0);
}

//  void QWidget::releaseMouse()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12releaseMouseEv(QWidget *self) {
  self->releaseMouse();
}

//  void QWidget::grabKeyboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12grabKeyboardEv(QWidget *self) {
  self->grabKeyboard();
}

//  void QWidget::releaseKeyboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15releaseKeyboardEv(QWidget *self) {
  self->releaseKeyboard();
}

//  int QWidget::grabShortcut(const QKeySequence &key, Qt::ShortcutContext
//      context)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QWidget12grabShortcutERK12QKeySequenceN2Qt15ShortcutContextE(
    QWidget *self,
    const QKeySequence *key,
    Qt::ShortcutContext context) {
  return self->grabShortcut(*key, context);
}

//  void QWidget::releaseShortcut(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15releaseShortcutEi(QWidget *self, int id) {
  self->releaseShortcut(id);
}

//  void QWidget::setShortcutEnabled(int id, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget18setShortcutEnabledEib(
    QWidget *self,
    int id,
    bool enable) {
  self->setShortcutEnabled(id, enable);
}

//  void QWidget::setShortcutAutoRepeat(int id, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget21setShortcutAutoRepeatEib(
    QWidget *self,
    int id,
    bool enable) {
  self->setShortcutAutoRepeat(id, enable);
}

//  QWidget *QWidget::mouseGrabber()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN7QWidget12mouseGrabberEv() {
  return QWidget::mouseGrabber();
}

//  QWidget *QWidget::keyboardGrabber()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN7QWidget15keyboardGrabberEv() {
  return QWidget::keyboardGrabber();
}

//  bool QWidget::updatesEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget14updatesEnabledEv(const QWidget *self) {
  return self->updatesEnabled();
}

//  void QWidget::setUpdatesEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17setUpdatesEnabledEb(QWidget *self, bool enable) {
  self->setUpdatesEnabled(enable);
}

//  QGraphicsProxyWidget *QWidget::graphicsProxyWidget() const
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZNK7QWidget19graphicsProxyWidgetEv(
    const QWidget *self) {
  return self->graphicsProxyWidget();
}

//  void QWidget::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6updateEv(QWidget *self) {
  self->update();
}

//  void QWidget::repaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7repaintEv(QWidget *self) {
  self->repaint();
}

//  void QWidget::update(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6updateEiiii(
    QWidget *self,
    int x,
    int y,
    int w,
    int h) {
  self->update(x, y, w, h);
}

//  void QWidget::update(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6updateERK5QRect(QWidget *self, const QRect *a0) {
  self->update(*a0);
}

//  void QWidget::update(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6updateERK7QRegion(QWidget *self, const QRegion *a0) {
  self->update(*a0);
}

//  void QWidget::repaint(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7repaintEiiii(
    QWidget *self,
    int x,
    int y,
    int w,
    int h) {
  self->repaint(x, y, w, h);
}

//  void QWidget::repaint(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7repaintERK5QRect(QWidget *self, const QRect *a0) {
  self->repaint(*a0);
}

//  void QWidget::repaint(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7repaintERK7QRegion(QWidget *self, const QRegion *a0) {
  self->repaint(*a0);
}

//  void QWidget::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10setVisibleEb(QWidget *self, bool visible) {
  self->setVisible(visible);
}

//  void QWidget::setHidden(bool hidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setHiddenEb(QWidget *self, bool hidden) {
  self->setHidden(hidden);
}

//  void QWidget::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget4showEv(QWidget *self) {
  self->show();
}

//  void QWidget::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget4hideEv(QWidget *self) {
  self->hide();
}

//  void QWidget::showMinimized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13showMinimizedEv(QWidget *self) {
  self->showMinimized();
}

//  void QWidget::showMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13showMaximizedEv(QWidget *self) {
  self->showMaximized();
}

//  void QWidget::showFullScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14showFullScreenEv(QWidget *self) {
  self->showFullScreen();
}

//  void QWidget::showNormal()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10showNormalEv(QWidget *self) {
  self->showNormal();
}

//  bool QWidget::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget5closeEv(QWidget *self) {
  return self->close();
}

//  void QWidget::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget5raiseEv(QWidget *self) {
  self->raise();
}

//  void QWidget::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget5lowerEv(QWidget *self) {
  self->lower();
}

//  void QWidget::stackUnder(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10stackUnderEPS_(QWidget *self, QWidget *a0) {
  self->stackUnder(a0);
}

//  void QWidget::move(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget4moveEii(QWidget *self, int x, int y) {
  self->move(x, y);
}

//  void QWidget::move(const QPoint &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget4moveERK6QPoint(QWidget *self, const QPoint *a0) {
  self->move(*a0);
}

//  void QWidget::resize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6resizeEii(QWidget *self, int w, int h) {
  self->resize(w, h);
}

//  void QWidget::resize(const QSize &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6resizeERK5QSize(QWidget *self, const QSize *a0) {
  self->resize(*a0);
}

//  void QWidget::setGeometry(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setGeometryEiiii(
    QWidget *self,
    int x,
    int y,
    int w,
    int h) {
  self->setGeometry(x, y, w, h);
}

//  void QWidget::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11setGeometryERK5QRect(
    QWidget *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QByteArray QWidget::saveGeometry() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QWidget12saveGeometryEv(const QWidget *self) {
  return new QByteArray(self->saveGeometry());
}

//  bool QWidget::restoreGeometry(const QByteArray &geometry)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget15restoreGeometryERK10QByteArray(
    QWidget *self,
    const QByteArray *geometry) {
  return self->restoreGeometry(*geometry);
}

//  void QWidget::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10adjustSizeEv(QWidget *self) {
  self->adjustSize();
}

//  bool QWidget::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget9isVisibleEv(const QWidget *self) {
  return self->isVisible();
}

//  bool QWidget::isVisibleTo(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget11isVisibleToEPKS_(
    const QWidget *self,
    const QWidget *a0) {
  return self->isVisibleTo(a0);
}

//  bool QWidget::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget8isHiddenEv(const QWidget *self) {
  return self->isHidden();
}

//  bool QWidget::isMinimized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget11isMinimizedEv(const QWidget *self) {
  return self->isMinimized();
}

//  bool QWidget::isMaximized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget11isMaximizedEv(const QWidget *self) {
  return self->isMaximized();
}

//  bool QWidget::isFullScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget12isFullScreenEv(const QWidget *self) {
  return self->isFullScreen();
}

//  Qt::WindowStates QWidget::windowState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget11windowStateEv(const QWidget *self) {
  return static_cast<int>(self->windowState().toInt());
}

//  void QWidget::setWindowState(Qt::WindowStates state)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setWindowStateE6QFlagsIN2Qt11WindowStateEE(
    QWidget *self,
    int state) {
  self->setWindowState(QFlags<Qt::WindowState>::fromInt(state));
}

//  void QWidget::overrideWindowState(Qt::WindowStates state)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget19overrideWindowStateE6QFlagsIN2Qt11WindowStateEE(
    QWidget *self,
    int state) {
  self->overrideWindowState(QFlags<Qt::WindowState>::fromInt(state));
}

//  QSize QWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget8sizeHintEv(const QWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWidget15minimumSizeHintEv(const QWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSizePolicy QWidget::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZNK7QWidget10sizePolicyEv(const QWidget *self) {
  return new QSizePolicy(self->sizePolicy());
}

//  void QWidget::setSizePolicy(QSizePolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setSizePolicyE11QSizePolicy(
    QWidget *self,
    const QSizePolicy *a0) {
  self->setSizePolicy(*a0);
}

//  void QWidget::setSizePolicy(QSizePolicy::Policy horizontal,
//      QSizePolicy::Policy vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setSizePolicyEN11QSizePolicy6PolicyES1_(
    QWidget *self,
    QSizePolicy::Policy horizontal,
    QSizePolicy::Policy vertical) {
  self->setSizePolicy(horizontal, vertical);
}

//  int QWidget::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget14heightForWidthEi(const QWidget *self, int a0) {
  return self->heightForWidth(a0);
}

//  bool QWidget::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget17hasHeightForWidthEv(const QWidget *self) {
  return self->hasHeightForWidth();
}

//  QRegion QWidget::visibleRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QWidget13visibleRegionEv(const QWidget *self) {
  return new QRegion(self->visibleRegion());
}

//  void QWidget::setContentsMargins(int left, int top, int right, int
//      bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget18setContentsMarginsEiiii(
    QWidget *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QWidget::setContentsMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget18setContentsMarginsERK8QMargins(
    QWidget *self,
    const QMargins *margins) {
  self->setContentsMargins(*margins);
}

//  QMargins QWidget::contentsMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QWidget15contentsMarginsEv(const QWidget *self) {
  return new QMargins(self->contentsMargins());
}

//  QRect QWidget::contentsRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWidget12contentsRectEv(const QWidget *self) {
  return new QRect(self->contentsRect());
}

//  QLayout *QWidget::layout() const
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZNK7QWidget6layoutEv(const QWidget *self) {
  return self->layout();
}

//  void QWidget::setLayout(QLayout *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setLayoutEP7QLayout(QWidget *self, QLayout *a0) {
  self->setLayout(a0);
}

//  void QWidget::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14updateGeometryEv(QWidget *self) {
  self->updateGeometry();
}

//  void QWidget::setParent(QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setParentEPS_(QWidget *self, QWidget *parent) {
  self->setParent(parent);
}

//  void QWidget::setParent(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setParentEPS_6QFlagsIN2Qt10WindowTypeEE(
    QWidget *self,
    QWidget *parent,
    int f) {
  self->setParent(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  void QWidget::scroll(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6scrollEii(QWidget *self, int dx, int dy) {
  self->scroll(dx, dy);
}

//  void QWidget::scroll(int dx, int dy, const QRect &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6scrollEiiRK5QRect(
    QWidget *self,
    int dx,
    int dy,
    const QRect *a2) {
  self->scroll(dx, dy, *a2);
}

//  QWidget *QWidget::focusWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget11focusWidgetEv(const QWidget *self) {
  return self->focusWidget();
}

//  QWidget *QWidget::nextInFocusChain() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget16nextInFocusChainEv(const QWidget *self) {
  return self->nextInFocusChain();
}

//  QWidget *QWidget::previousInFocusChain() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget20previousInFocusChainEv(const QWidget *self) {
  return self->previousInFocusChain();
}

//  bool QWidget::acceptDrops() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget11acceptDropsEv(const QWidget *self) {
  return self->acceptDrops();
}

//  void QWidget::setAcceptDrops(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setAcceptDropsEb(QWidget *self, bool on) {
  self->setAcceptDrops(on);
}

//  void QWidget::addAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9addActionEP7QAction(QWidget *self, QAction *action) {
  self->addAction(action);
}

//  void QWidget::addActions(const QList<QAction *> &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10addActionsERK5QListIP7QActionE(
    QWidget *self,
    const QList<QAction *> *actions) {
  self->addActions(*actions);
}

//  void QWidget::insertActions(QAction *before, const QList<QAction *>
//      &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13insertActionsEP7QActionRK5QListIS1_E(
    QWidget *self,
    QAction *before,
    const QList<QAction *> *actions) {
  self->insertActions(before, *actions);
}

//  void QWidget::insertAction(QAction *before, QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12insertActionEP7QActionS1_(
    QWidget *self,
    QAction *before,
    QAction *action) {
  self->insertAction(before, action);
}

//  void QWidget::removeAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12removeActionEP7QAction(
    QWidget *self,
    QAction *action) {
  self->removeAction(action);
}

//  QList<QAction *> QWidget::actions() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK7QWidget7actionsEv(const QWidget *self) {
  return new QList<QAction *>(self->actions());
}

//  QAction *QWidget::addAction(const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK7QString(
    QWidget *self,
    const QString *text) {
  return self->addAction(*text);
}

//  QAction *QWidget::addAction(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK5QIconRK7QString(
    QWidget *self,
    const QIcon *icon,
    const QString *text) {
  return self->addAction(*icon, *text);
}

//  QAction *QWidget::addAction(const QString &text, const QObject *receiver,
//      const char *member, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK7QStringPK7QObjectPKcN2Qt14ConnectionTypeE(
    QWidget *self,
    const QString *text,
    const QObject *receiver,
    const char *member,
    Qt::ConnectionType type) {
  return self->addAction(*text, receiver, member, type);
}

//  QAction *QWidget::addAction(const QIcon &icon, const QString &text, const
//      QObject *receiver, const char *member, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK5QIconRK7QStringPK7QObjectPKcN2Qt14ConnectionTypeE(
    QWidget *self,
    const QIcon *icon,
    const QString *text,
    const QObject *receiver,
    const char *member,
    Qt::ConnectionType type) {
  return self->addAction(*icon, *text, receiver, member, type);
}

//  QAction *QWidget::addAction(const QString &text, const QKeySequence
//      &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK7QStringRK12QKeySequence(
    QWidget *self,
    const QString *text,
    const QKeySequence *shortcut) {
  return self->addAction(*text, *shortcut);
}

//  QAction *QWidget::addAction(const QIcon &icon, const QString &text, const
//      QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK5QIconRK7QStringRK12QKeySequence(
    QWidget *self,
    const QIcon *icon,
    const QString *text,
    const QKeySequence *shortcut) {
  return self->addAction(*icon, *text, *shortcut);
}

//  QAction *QWidget::addAction(const QString &text, const QKeySequence
//      &shortcut, const QObject *receiver, const char *member,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK7QStringRK12QKeySequencePK7QObjectPKcN2Qt14ConnectionTypeE(
    QWidget *self,
    const QString *text,
    const QKeySequence *shortcut,
    const QObject *receiver,
    const char *member,
    Qt::ConnectionType type) {
  return self->addAction(*text, *shortcut, receiver, member, type);
}

//  QAction *QWidget::addAction(const QIcon &icon, const QString &text, const
//      QKeySequence &shortcut, const QObject *receiver, const char *member,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN7QWidget9addActionERK5QIconRK7QStringRK12QKeySequencePK7QObjectPKcN2Qt14ConnectionTypeE(
    QWidget *self,
    const QIcon *icon,
    const QString *text,
    const QKeySequence *shortcut,
    const QObject *receiver,
    const char *member,
    Qt::ConnectionType type) {
  return self->addAction(*icon, *text, *shortcut, receiver, member, type);
}

//  QWidget *QWidget::parentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget12parentWidgetEv(const QWidget *self) {
  return self->parentWidget();
}

//  void QWidget::setWindowFlags(Qt::WindowFlags type)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWidget *self,
    int type) {
  self->setWindowFlags(QFlags<Qt::WindowType>::fromInt(type));
}

//  Qt::WindowFlags QWidget::windowFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget11windowFlagsEv(const QWidget *self) {
  return static_cast<int>(self->windowFlags().toInt());
}

//  void QWidget::setWindowFlag(Qt::WindowType a0, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13setWindowFlagEN2Qt10WindowTypeEb(
    QWidget *self,
    Qt::WindowType a0,
    bool on) {
  self->setWindowFlag(a0, on);
}

//  void QWidget::overrideWindowFlags(Qt::WindowFlags type)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget19overrideWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWidget *self,
    int type) {
  self->overrideWindowFlags(QFlags<Qt::WindowType>::fromInt(type));
}

//  Qt::WindowType QWidget::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK7QWidget10windowTypeEv(const QWidget *self) {
  return self->windowType();
}

//  QWidget *QWidget::find(WId a0)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN7QWidget4findEy(WId a0) {
  return QWidget::find(a0);
}

//  QWidget *QWidget::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget7childAtEii(const QWidget *self, int x, int y) {
  return self->childAt(x, y);
}

//  QWidget *QWidget::childAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget7childAtERK6QPoint(
    const QWidget *self,
    const QPoint *p) {
  return self->childAt(*p);
}

//  QWidget *QWidget::childAt(const QPointF &p) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWidget7childAtERK7QPointF(
    const QWidget *self,
    const QPointF *p) {
  return self->childAt(*p);
}

//  void QWidget::setAttribute(Qt::WidgetAttribute a0, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12setAttributeEN2Qt15WidgetAttributeEb(
    QWidget *self,
    Qt::WidgetAttribute a0,
    bool on) {
  self->setAttribute(a0, on);
}

//  bool QWidget::testAttribute(Qt::WidgetAttribute a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget13testAttributeEN2Qt15WidgetAttributeE(
    const QWidget *self,
    Qt::WidgetAttribute a0) {
  return self->testAttribute(a0);
}

//  QPaintEngine *QWidget::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK7QWidget11paintEngineEv(const QWidget *self) {
  return self->paintEngine();
}

//  void QWidget::ensurePolished() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QWidget14ensurePolishedEv(const QWidget *self) {
  self->ensurePolished();
}

//  bool QWidget::isAncestorOf(const QWidget *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget12isAncestorOfEPKS_(
    const QWidget *self,
    const QWidget *child) {
  return self->isAncestorOf(child);
}

//  bool QWidget::autoFillBackground() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget18autoFillBackgroundEv(const QWidget *self) {
  return self->autoFillBackground();
}

//  void QWidget::setAutoFillBackground(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget21setAutoFillBackgroundEb(
    QWidget *self,
    bool enabled) {
  self->setAutoFillBackground(enabled);
}

//  QBackingStore *QWidget::backingStore() const
extern "C" Q_DECL_EXPORT
QBackingStore *ritual_ZNK7QWidget12backingStoreEv(const QWidget *self) {
  return self->backingStore();
}

//  QWindow *QWidget::windowHandle() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK7QWidget12windowHandleEv(const QWidget *self) {
  return self->windowHandle();
}

//  QScreen *QWidget::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK7QWidget6screenEv(const QWidget *self) {
  return self->screen();
}

//  void QWidget::setScreen(QScreen *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9setScreenEP7QScreen(QWidget *self, QScreen *a0) {
  self->setScreen(a0);
}

//  QWidget *QWidget::createWindowContainer(QWindow *window, QWidget *parent,
//      Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN7QWidget21createWindowContainerEP7QWindowPS_6QFlagsIN2Qt10WindowTypeEE(
    QWindow *window,
    QWidget *parent,
    int flags) {
  return QWidget::createWindowContainer(
      window,
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  bool QWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget5eventEP6QEvent(QWidget *self, QEvent *event) {
  return self->event(event);
}

//  void QWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15mousePressEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QWidget::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget17mouseReleaseEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QWidget::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14mouseMoveEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QWidget::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10wheelEventEP11QWheelEvent(
    QWidget *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}

//  void QWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13keyPressEventEP9QKeyEvent(
    QWidget *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QWidget::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15keyReleaseEventEP9QKeyEvent(
    QWidget *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget12focusInEventEP11QFocusEvent(
    QWidget *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13focusOutEventEP11QFocusEvent(
    QWidget *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QWidget::enterEvent(QEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10enterEventEP11QEnterEvent(
    QWidget *self,
    QEnterEvent *event) {
  self->enterEvent(event);
}

//  void QWidget::leaveEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10leaveEventEP6QEvent(QWidget *self, QEvent *event) {
  self->leaveEvent(event);
}

//  void QWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10paintEventEP11QPaintEvent(
    QWidget *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QWidget::moveEvent(QMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9moveEventEP10QMoveEvent(
    QWidget *self,
    QMoveEvent *event) {
  self->moveEvent(event);
}

//  void QWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11resizeEventEP12QResizeEvent(
    QWidget *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QWidget::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget10closeEventEP11QCloseEvent(
    QWidget *self,
    QCloseEvent *event) {
  self->closeEvent(event);
}

//  void QWidget::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16contextMenuEventEP17QContextMenuEvent(
    QWidget *self,
    QContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void QWidget::tabletEvent(QTabletEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11tabletEventEP12QTabletEvent(
    QWidget *self,
    QTabletEvent *event) {
  self->tabletEvent(event);
}

//  void QWidget::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11actionEventEP12QActionEvent(
    QWidget *self,
    QActionEvent *event) {
  self->actionEvent(event);
}

//  void QWidget::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14dragEnterEventEP15QDragEnterEvent(
    QWidget *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}

//  void QWidget::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget13dragMoveEventEP14QDragMoveEvent(
    QWidget *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}

//  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent(
    QWidget *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9dropEventEP10QDropEvent(
    QWidget *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  void QWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9showEventEP10QShowEvent(
    QWidget *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget9hideEventEP10QHideEvent(
    QWidget *self,
    QHideEvent *event) {
  self->hideEvent(event);
}

//  void QWidget::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget11changeEventEP6QEvent(QWidget *self, QEvent *a0) {
  self->changeEvent(a0);
}

//  int QWidget::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QWidget *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return self->metric(a0);
}

//  void QWidget::initPainter(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QWidget11initPainterEP8QPainter(
    const QWidget *self,
    QPainter *painter) {
  self->initPainter(painter);
}

//  QPaintDevice *QWidget::redirected(QPoint *offset) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK7QWidget10redirectedEP6QPoint(
    const QWidget *self,
    QPoint *offset) {
  return self->redirected(offset);
}

//  QPainter *QWidget::sharedPainter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZNK7QWidget13sharedPainterEv(const QWidget *self) {
  return self->sharedPainter();
}

//  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16inputMethodEventEP17QInputMethodEvent(
    QWidget *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}

//  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QWidget *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  Qt::InputMethodHints QWidget::inputMethodHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWidget16inputMethodHintsEv(const QWidget *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QWidget::setInputMethodHints(Qt::InputMethodHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHintEE(
    QWidget *self,
    int hints) {
  self->setInputMethodHints(QFlags<Qt::InputMethodHint>::fromInt(hints));
}

//  void QWidget::updateMicroFocus(Qt::InputMethodQuery query)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget16updateMicroFocusEN2Qt16InputMethodQueryE(
    QWidget *self,
    Qt::InputMethodQuery query) {
  self->updateMicroFocus(query);
}

//  void QWidget::create(WId a0, bool initializeWindow, bool
//      destroyOldWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget6createEybb(
    QWidget *self,
    WId a0,
    bool initializeWindow,
    bool destroyOldWindow) {
  self->create(a0, initializeWindow, destroyOldWindow);
}

//  void QWidget::destroy(bool destroyWindow, bool destroySubWindows)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget7destroyEbb(
    QWidget *self,
    bool destroyWindow,
    bool destroySubWindows) {
  self->destroy(destroyWindow, destroySubWindows);
}

//  bool QWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget18focusNextPrevChildEb(QWidget *self, bool next) {
  return self->focusNextPrevChild(next);
}

//  bool QWidget::focusNextChild()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget14focusNextChildEv(QWidget *self) {
  return self->focusNextChild();
}

//  bool QWidget::focusPreviousChild()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWidget18focusPreviousChildEv(QWidget *self) {
  return self->focusPreviousChild();
}

//  void QWidget::setBackingStore(QBackingStore *store)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWidget15setBackingStoreEP13QBackingStore(
    QWidget *self,
    QBackingStore *store) {
  self->setBackingStore(store);
}

//  bool QWidget::testAttribute_helper(Qt::WidgetAttribute a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWidget20testAttribute_helperEN2Qt15WidgetAttributeE(
    const QWidget *self,
    Qt::WidgetAttribute a0) {
  return self->testAttribute_helper(a0);
}

//  QLayout *QWidget::takeLayout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN7QWidget10takeLayoutEv(QWidget *self) {
  return self->takeLayout();
}

//  QWidget as the QPaintDevice it is built on
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_cast_QWidget_QPaintDevice(QWidget *self) {
  return static_cast<QPaintDevice *>(self);
}

//  a Python function taken by a CuteQWidget, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidget(QWidget *self, const char *key, void *call) {
  return static_cast<CuteQWidget *>(self)->take(key, call);
}

//  int QWidget::devType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QWidget7devTypeEv(const QWidget *self) {
  return self->QWidget::devType();
}

//  void QWidget::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10setVisibleEb(QWidget *self, bool visible) {
  self->QWidget::setVisible(visible);
}

//  QSize QWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QWidget8sizeHintEv(const QWidget *self) {
  return new QSize(self->QWidget::sizeHint());
}

//  QSize QWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QWidget15minimumSizeHintEv(const QWidget *self) {
  return new QSize(self->QWidget::minimumSizeHint());
}

//  int QWidget::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QWidget14heightForWidthEi(const QWidget *self, int a0) {
  return self->QWidget::heightForWidth(a0);
}

//  bool QWidget::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK7QWidget17hasHeightForWidthEv(const QWidget *self) {
  return self->QWidget::hasHeightForWidth();
}

//  QPaintEngine *QWidget::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK7QWidget11paintEngineEv(const QWidget *self) {
  return self->QWidget::paintEngine();
}

//  bool QWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QWidget5eventEP6QEvent(QWidget *self, QEvent *event) {
  return static_cast<OwnQWidget *>(self)->OwnQWidget::event(event);
}

//  void QWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget15mousePressEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::mousePressEvent(event);
}

//  void QWidget::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget17mouseReleaseEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::mouseReleaseEvent(event);
}

//  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::mouseDoubleClickEvent(event);
}

//  void QWidget::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget14mouseMoveEventEP11QMouseEvent(
    QWidget *self,
    QMouseEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::mouseMoveEvent(event);
}

//  void QWidget::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10wheelEventEP11QWheelEvent(
    QWidget *self,
    QWheelEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::wheelEvent(event);
}

//  void QWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget13keyPressEventEP9QKeyEvent(
    QWidget *self,
    QKeyEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::keyPressEvent(event);
}

//  void QWidget::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget15keyReleaseEventEP9QKeyEvent(
    QWidget *self,
    QKeyEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::keyReleaseEvent(event);
}

//  void QWidget::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget12focusInEventEP11QFocusEvent(
    QWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::focusInEvent(event);
}

//  void QWidget::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget13focusOutEventEP11QFocusEvent(
    QWidget *self,
    QFocusEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::focusOutEvent(event);
}

//  void QWidget::enterEvent(QEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10enterEventEP11QEnterEvent(
    QWidget *self,
    QEnterEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::enterEvent(event);
}

//  void QWidget::leaveEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10leaveEventEP6QEvent(
    QWidget *self,
    QEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::leaveEvent(event);
}

//  void QWidget::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10paintEventEP11QPaintEvent(
    QWidget *self,
    QPaintEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::paintEvent(event);
}

//  void QWidget::moveEvent(QMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget9moveEventEP10QMoveEvent(
    QWidget *self,
    QMoveEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::moveEvent(event);
}

//  void QWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget11resizeEventEP12QResizeEvent(
    QWidget *self,
    QResizeEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::resizeEvent(event);
}

//  void QWidget::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget10closeEventEP11QCloseEvent(
    QWidget *self,
    QCloseEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::closeEvent(event);
}

//  void QWidget::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget16contextMenuEventEP17QContextMenuEvent(
    QWidget *self,
    QContextMenuEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::contextMenuEvent(event);
}

//  void QWidget::tabletEvent(QTabletEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget11tabletEventEP12QTabletEvent(
    QWidget *self,
    QTabletEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::tabletEvent(event);
}

//  void QWidget::actionEvent(QActionEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget11actionEventEP12QActionEvent(
    QWidget *self,
    QActionEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::actionEvent(event);
}

//  void QWidget::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget14dragEnterEventEP15QDragEnterEvent(
    QWidget *self,
    QDragEnterEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::dragEnterEvent(event);
}

//  void QWidget::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget13dragMoveEventEP14QDragMoveEvent(
    QWidget *self,
    QDragMoveEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::dragMoveEvent(event);
}

//  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent(
    QWidget *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::dragLeaveEvent(event);
}

//  void QWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget9dropEventEP10QDropEvent(
    QWidget *self,
    QDropEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::dropEvent(event);
}

//  void QWidget::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget9showEventEP10QShowEvent(
    QWidget *self,
    QShowEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::showEvent(event);
}

//  void QWidget::hideEvent(QHideEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget9hideEventEP10QHideEvent(
    QWidget *self,
    QHideEvent *event) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::hideEvent(event);
}

//  void QWidget::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget11changeEventEP6QEvent(QWidget *self, QEvent *a0) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::changeEvent(a0);
}

//  int QWidget::metric(PaintDeviceMetric a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QWidget6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QWidget *self,
    QPaintDevice::PaintDeviceMetric a0) {
  return static_cast<const OwnQWidget *>(self)->OwnQWidget::metric(a0);
}

//  void QWidget::initPainter(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK7QWidget11initPainterEP8QPainter(
    const QWidget *self,
    QPainter *painter) {
  static_cast<const OwnQWidget *>(self)->OwnQWidget::initPainter(painter);
}

//  QPaintDevice *QWidget::redirected(QPoint *offset) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZNK7QWidget10redirectedEP6QPoint(
    const QWidget *self,
    QPoint *offset) {
  return static_cast<const OwnQWidget *>(self)->OwnQWidget::redirected(
      offset);
}

//  QPainter *QWidget::sharedPainter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_own_ZNK7QWidget13sharedPainterEv(const QWidget *self) {
  return static_cast<const OwnQWidget *>(self)->OwnQWidget::sharedPainter();
}

//  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWidget16inputMethodEventEP17QInputMethodEvent(
    QWidget *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQWidget *>(self)->OwnQWidget::inputMethodEvent(a0);
}

//  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QWidget *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->QWidget::inputMethodQuery(a0));
}

//  bool QWidget::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QWidget18focusNextPrevChildEb(QWidget *self, bool next) {
  return static_cast<OwnQWidget *>(self)->OwnQWidget::focusNextPrevChild(
      next);
}

//  QList<QWidget *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_list_make_QWidget_ptr() {
  return new QList<QWidget *>();
}

//  void QList<QWidget *>::append(const QWidget * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWidget_ptr(QList<QWidget *> *self, QWidget *element) {
  self->append(element);
}

//  qsizetype QList<QWidget *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWidget_ptr(const QList<QWidget *> *self) {
  return self->size();
}

//  const QWidget * &QList<QWidget *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_list_at_QWidget_ptr(
    const QList<QWidget *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWidget *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWidget_ptr(QList<QWidget *> *self) {
  delete self;
}
