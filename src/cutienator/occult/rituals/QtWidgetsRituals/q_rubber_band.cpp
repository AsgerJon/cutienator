//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qrubberband.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qrubberband.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRubberBand may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRubberBand : QRubberBand {
  using QRubberBand::event;
  using QRubberBand::paintEvent;
  using QRubberBand::changeEvent;
  using QRubberBand::showEvent;
  using QRubberBand::resizeEvent;
  using QRubberBand::moveEvent;
  using QRubberBand::initStyleOption;
};

//  A QRubberBand that Python can take functions over in. Every QRubberBand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRubberBandCall0)(const void *, QEvent *, int *);
typedef void (*CuteQRubberBandCall1)(const void *, QPaintEvent *, int *);
typedef void (*CuteQRubberBandCall2)(const void *, QEvent *, int *);
typedef void (*CuteQRubberBandCall3)(const void *, QShowEvent *, int *);
typedef void (*CuteQRubberBandCall4)(const void *, QResizeEvent *, int *);
typedef void (*CuteQRubberBandCall5)(const void *, QMoveEvent *, int *);
typedef void (*CuteQRubberBandCall6)(const void *, QStyleOptionRubberBand *, int *);
typedef int (*CuteQRubberBandCall7)(const void *, int *);
typedef void (*CuteQRubberBandCall8)(const void *, bool, int *);
typedef const QSize * (*CuteQRubberBandCall9)(const void *, int *);
typedef const QSize * (*CuteQRubberBandCall10)(const void *, int *);
typedef int (*CuteQRubberBandCall11)(const void *, int, int *);
typedef bool (*CuteQRubberBandCall12)(const void *, int *);
typedef void * (*CuteQRubberBandCall13)(const void *, int *);
typedef void (*CuteQRubberBandCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRubberBandCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRubberBandCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRubberBandCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQRubberBandCall18)(const void *, QWheelEvent *, int *);
typedef void (*CuteQRubberBandCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRubberBandCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQRubberBandCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRubberBandCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQRubberBandCall23)(const void *, QEnterEvent *, int *);
typedef void (*CuteQRubberBandCall24)(const void *, QEvent *, int *);
typedef void (*CuteQRubberBandCall25)(const void *, QCloseEvent *, int *);
typedef void (*CuteQRubberBandCall26)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQRubberBandCall27)(const void *, QTabletEvent *, int *);
typedef void (*CuteQRubberBandCall28)(const void *, QActionEvent *, int *);
typedef void (*CuteQRubberBandCall29)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQRubberBandCall30)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQRubberBandCall31)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQRubberBandCall32)(const void *, QDropEvent *, int *);
typedef void (*CuteQRubberBandCall33)(const void *, QHideEvent *, int *);
typedef int (*CuteQRubberBandCall34)(const void *, int, int *);
typedef void (*CuteQRubberBandCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQRubberBandCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQRubberBandCall37)(const void *, int *);
typedef void (*CuteQRubberBandCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQRubberBandCall39)(const void *, int, int *);
typedef bool (*CuteQRubberBandCall40)(const void *, bool, int *);
typedef bool (*CuteQRubberBandCall41)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQRubberBandCall42)(const void *, QTimerEvent *, int *);
typedef void (*CuteQRubberBandCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQRubberBandCall44)(const void *, QEvent *, int *);
typedef void (*CuteQRubberBandCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQRubberBandCall46)(const void *, const QMetaMethod *, int *);
class CuteQRubberBand : public QRubberBand {
public:
  using QRubberBand::QRubberBand;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
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
    if (!std::strcmp(key, "_ZNK11QRubberBand15initStyleOptionEP22QStyleOptionRubberBand")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  bool QRubberBand::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRubberBandCall0 call = reinterpret_cast<CuteQRubberBandCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QRubberBand::event(e);
  }

  //  void QRubberBand::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRubberBandCall1 call = reinterpret_cast<CuteQRubberBandCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRubberBand::paintEvent(a0);
  }

  //  void QRubberBand::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRubberBandCall2 call = reinterpret_cast<CuteQRubberBandCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRubberBand::changeEvent(a0);
  }

  //  void QRubberBand::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRubberBandCall3 call = reinterpret_cast<CuteQRubberBandCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRubberBand::showEvent(a0);
  }

  //  void QRubberBand::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRubberBandCall4 call = reinterpret_cast<CuteQRubberBandCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRubberBand::resizeEvent(a0);
  }

  //  void QRubberBand::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRubberBandCall5 call = reinterpret_cast<CuteQRubberBandCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRubberBand::moveEvent(a0);
  }

  //  void QRubberBand::initStyleOption(QStyleOptionRubberBand *option)
  //      const
  void initStyleOption(QStyleOptionRubberBand *option) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRubberBandCall6 call = reinterpret_cast<CuteQRubberBandCall6>(taken[6]);
      call(this, option, &handled);
      if (handled) return;
    }
    QRubberBand::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQRubberBandCall7 call = reinterpret_cast<CuteQRubberBandCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRubberBandCall8 call = reinterpret_cast<CuteQRubberBandCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRubberBandCall9 call = reinterpret_cast<CuteQRubberBandCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQRubberBandCall10 call = reinterpret_cast<CuteQRubberBandCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRubberBandCall11 call = reinterpret_cast<CuteQRubberBandCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQRubberBandCall12 call = reinterpret_cast<CuteQRubberBandCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQRubberBandCall13 call = reinterpret_cast<CuteQRubberBandCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRubberBandCall14 call = reinterpret_cast<CuteQRubberBandCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQRubberBandCall15 call = reinterpret_cast<CuteQRubberBandCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRubberBandCall16 call = reinterpret_cast<CuteQRubberBandCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRubberBandCall17 call = reinterpret_cast<CuteQRubberBandCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRubberBandCall18 call = reinterpret_cast<CuteQRubberBandCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRubberBandCall19 call = reinterpret_cast<CuteQRubberBandCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRubberBandCall20 call = reinterpret_cast<CuteQRubberBandCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRubberBandCall21 call = reinterpret_cast<CuteQRubberBandCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRubberBandCall22 call = reinterpret_cast<CuteQRubberBandCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRubberBandCall23 call = reinterpret_cast<CuteQRubberBandCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRubberBandCall24 call = reinterpret_cast<CuteQRubberBandCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRubberBandCall25 call = reinterpret_cast<CuteQRubberBandCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRubberBandCall26 call = reinterpret_cast<CuteQRubberBandCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRubberBandCall27 call = reinterpret_cast<CuteQRubberBandCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRubberBandCall28 call = reinterpret_cast<CuteQRubberBandCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRubberBandCall29 call = reinterpret_cast<CuteQRubberBandCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRubberBandCall30 call = reinterpret_cast<CuteQRubberBandCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRubberBandCall31 call = reinterpret_cast<CuteQRubberBandCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRubberBandCall32 call = reinterpret_cast<CuteQRubberBandCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRubberBandCall33 call = reinterpret_cast<CuteQRubberBandCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQRubberBandCall34 call = reinterpret_cast<CuteQRubberBandCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQRubberBandCall35 call = reinterpret_cast<CuteQRubberBandCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQRubberBandCall36 call = reinterpret_cast<CuteQRubberBandCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQRubberBandCall37 call = reinterpret_cast<CuteQRubberBandCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRubberBandCall38 call = reinterpret_cast<CuteQRubberBandCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQRubberBandCall39 call = reinterpret_cast<CuteQRubberBandCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQRubberBandCall40 call = reinterpret_cast<CuteQRubberBandCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQRubberBandCall41 call = reinterpret_cast<CuteQRubberBandCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQRubberBandCall42 call = reinterpret_cast<CuteQRubberBandCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQRubberBandCall43 call = reinterpret_cast<CuteQRubberBandCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQRubberBandCall44 call = reinterpret_cast<CuteQRubberBandCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQRubberBandCall45 call = reinterpret_cast<CuteQRubberBandCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQRubberBandCall46 call = reinterpret_cast<CuteQRubberBandCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QRubberBand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QRubberBand10metaObjectEv(
    const QRubberBand *self) {
  return self->metaObject();
}

//  QString QRubberBand::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QRubberBand2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRubberBand::tr(s, c, n));
}

//  QRubberBand::QRubberBand(Shape a0, QWidget *a1)
extern "C" Q_DECL_EXPORT
QRubberBand *ritual_ZN11QRubberBandC1ENS_5ShapeEP7QWidget(
    QRubberBand::Shape a0,
    QWidget *a1) {
  return new CuteQRubberBand(a0, a1);
}

//  QRubberBand::~QRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBandD1Ev(QRubberBand *self) {
  delete self;
}

//  Shape QRubberBand::shape() const
extern "C" Q_DECL_EXPORT
QRubberBand::Shape ritual_ZNK11QRubberBand5shapeEv(const QRubberBand *self) {
  return self->shape();
}

//  void QRubberBand::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand11setGeometryERK5QRect(
    QRubberBand *self,
    const QRect *r) {
  self->setGeometry(*r);
}

//  void QRubberBand::setGeometry(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand11setGeometryEiiii(
    QRubberBand *self,
    int x,
    int y,
    int w,
    int h) {
  self->setGeometry(x, y, w, h);
}

//  void QRubberBand::move(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand4moveEii(QRubberBand *self, int x, int y) {
  self->move(x, y);
}

//  void QRubberBand::move(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand4moveERK6QPoint(
    QRubberBand *self,
    const QPoint *p) {
  self->move(*p);
}

//  void QRubberBand::resize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand6resizeEii(QRubberBand *self, int w, int h) {
  self->resize(w, h);
}

//  void QRubberBand::resize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand6resizeERK5QSize(
    QRubberBand *self,
    const QSize *s) {
  self->resize(*s);
}

//  a Python function taken by a CuteQRubberBand, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRubberBand(
    QRubberBand *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRubberBand *>(self)->take(key, call);
}

//  bool QRubberBand::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRubberBand5eventEP6QEvent(
    QRubberBand *self,
    QEvent *e) {
  return static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::event(e);
}

//  void QRubberBand::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRubberBand10paintEventEP11QPaintEvent(
    QRubberBand *self,
    QPaintEvent *a0) {
  static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::paintEvent(a0);
}

//  void QRubberBand::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRubberBand11changeEventEP6QEvent(
    QRubberBand *self,
    QEvent *a0) {
  static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::changeEvent(a0);
}

//  void QRubberBand::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRubberBand9showEventEP10QShowEvent(
    QRubberBand *self,
    QShowEvent *a0) {
  static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::showEvent(a0);
}

//  void QRubberBand::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRubberBand11resizeEventEP12QResizeEvent(
    QRubberBand *self,
    QResizeEvent *a0) {
  static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::resizeEvent(a0);
}

//  void QRubberBand::moveEvent(QMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRubberBand9moveEventEP10QMoveEvent(
    QRubberBand *self,
    QMoveEvent *a0) {
  static_cast<OwnQRubberBand *>(self)->OwnQRubberBand::moveEvent(a0);
}

//  void QRubberBand::initStyleOption(QStyleOptionRubberBand *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QRubberBand15initStyleOptionEP22QStyleOptionRubberBand(
    const QRubberBand *self,
    QStyleOptionRubberBand *option) {
  static_cast<const OwnQRubberBand *>(self)->OwnQRubberBand::initStyleOption(
      option);
}
