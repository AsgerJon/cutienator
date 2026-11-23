//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdialogbuttonbox.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qabstractbutton.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QDialogButtonBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDialogButtonBox : QDialogButtonBox {
  using QDialogButtonBox::changeEvent;
  using QDialogButtonBox::event;
};

//  A QDialogButtonBox that Python can take functions over in. Every QDialogButtonBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDialogButtonBoxCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQDialogButtonBoxCall1)(const void *, QEvent *, int *);
typedef int (*CuteQDialogButtonBoxCall2)(const void *, int *);
typedef void (*CuteQDialogButtonBoxCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQDialogButtonBoxCall4)(const void *, int *);
typedef const QSize * (*CuteQDialogButtonBoxCall5)(const void *, int *);
typedef int (*CuteQDialogButtonBoxCall6)(const void *, int, int *);
typedef bool (*CuteQDialogButtonBoxCall7)(const void *, int *);
typedef void * (*CuteQDialogButtonBoxCall8)(const void *, int *);
typedef void (*CuteQDialogButtonBoxCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall13)(const void *, QWheelEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall19)(const void *, QEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall23)(const void *, QCloseEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall24)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall25)(const void *, QTabletEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall26)(const void *, QActionEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall27)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall28)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall29)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall30)(const void *, QDropEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall32)(const void *, QHideEvent *, int *);
typedef int (*CuteQDialogButtonBoxCall33)(const void *, int, int *);
typedef void (*CuteQDialogButtonBoxCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQDialogButtonBoxCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQDialogButtonBoxCall36)(const void *, int *);
typedef void (*CuteQDialogButtonBoxCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDialogButtonBoxCall38)(const void *, int, int *);
typedef bool (*CuteQDialogButtonBoxCall39)(const void *, bool, int *);
typedef bool (*CuteQDialogButtonBoxCall40)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall41)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall42)(const void *, QChildEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall43)(const void *, QEvent *, int *);
typedef void (*CuteQDialogButtonBoxCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDialogButtonBoxCall45)(const void *, const QMetaMethod *, int *);
class CuteQDialogButtonBox : public QDialogButtonBox {
public:
  using QDialogButtonBox::QDialogButtonBox;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
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
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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

  //  void QDialogButtonBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDialogButtonBoxCall0 call = reinterpret_cast<CuteQDialogButtonBoxCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QDialogButtonBox::changeEvent(event);
  }

  //  bool QDialogButtonBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDialogButtonBoxCall1 call = reinterpret_cast<CuteQDialogButtonBoxCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QDialogButtonBox::event(event);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDialogButtonBoxCall2 call = reinterpret_cast<CuteQDialogButtonBoxCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDialogButtonBoxCall3 call = reinterpret_cast<CuteQDialogButtonBoxCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDialogButtonBoxCall4 call = reinterpret_cast<CuteQDialogButtonBoxCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDialogButtonBoxCall5 call = reinterpret_cast<CuteQDialogButtonBoxCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDialogButtonBoxCall6 call = reinterpret_cast<CuteQDialogButtonBoxCall6>(taken[6]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDialogButtonBoxCall7 call = reinterpret_cast<CuteQDialogButtonBoxCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDialogButtonBoxCall8 call = reinterpret_cast<CuteQDialogButtonBoxCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDialogButtonBoxCall9 call = reinterpret_cast<CuteQDialogButtonBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDialogButtonBoxCall10 call = reinterpret_cast<CuteQDialogButtonBoxCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDialogButtonBoxCall11 call = reinterpret_cast<CuteQDialogButtonBoxCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDialogButtonBoxCall12 call = reinterpret_cast<CuteQDialogButtonBoxCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDialogButtonBoxCall13 call = reinterpret_cast<CuteQDialogButtonBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDialogButtonBoxCall14 call = reinterpret_cast<CuteQDialogButtonBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDialogButtonBoxCall15 call = reinterpret_cast<CuteQDialogButtonBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDialogButtonBoxCall16 call = reinterpret_cast<CuteQDialogButtonBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDialogButtonBoxCall17 call = reinterpret_cast<CuteQDialogButtonBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDialogButtonBoxCall18 call = reinterpret_cast<CuteQDialogButtonBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDialogButtonBoxCall19 call = reinterpret_cast<CuteQDialogButtonBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDialogButtonBoxCall20 call = reinterpret_cast<CuteQDialogButtonBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDialogButtonBoxCall21 call = reinterpret_cast<CuteQDialogButtonBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDialogButtonBoxCall22 call = reinterpret_cast<CuteQDialogButtonBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDialogButtonBoxCall23 call = reinterpret_cast<CuteQDialogButtonBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDialogButtonBoxCall24 call = reinterpret_cast<CuteQDialogButtonBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDialogButtonBoxCall25 call = reinterpret_cast<CuteQDialogButtonBoxCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDialogButtonBoxCall26 call = reinterpret_cast<CuteQDialogButtonBoxCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDialogButtonBoxCall27 call = reinterpret_cast<CuteQDialogButtonBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDialogButtonBoxCall28 call = reinterpret_cast<CuteQDialogButtonBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDialogButtonBoxCall29 call = reinterpret_cast<CuteQDialogButtonBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDialogButtonBoxCall30 call = reinterpret_cast<CuteQDialogButtonBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDialogButtonBoxCall31 call = reinterpret_cast<CuteQDialogButtonBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDialogButtonBoxCall32 call = reinterpret_cast<CuteQDialogButtonBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQDialogButtonBoxCall33 call = reinterpret_cast<CuteQDialogButtonBoxCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQDialogButtonBoxCall34 call = reinterpret_cast<CuteQDialogButtonBoxCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQDialogButtonBoxCall35 call = reinterpret_cast<CuteQDialogButtonBoxCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQDialogButtonBoxCall36 call = reinterpret_cast<CuteQDialogButtonBoxCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDialogButtonBoxCall37 call = reinterpret_cast<CuteQDialogButtonBoxCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQDialogButtonBoxCall38 call = reinterpret_cast<CuteQDialogButtonBoxCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDialogButtonBoxCall39 call = reinterpret_cast<CuteQDialogButtonBoxCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDialogButtonBoxCall40 call = reinterpret_cast<CuteQDialogButtonBoxCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDialogButtonBoxCall41 call = reinterpret_cast<CuteQDialogButtonBoxCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDialogButtonBoxCall42 call = reinterpret_cast<CuteQDialogButtonBoxCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDialogButtonBoxCall43 call = reinterpret_cast<CuteQDialogButtonBoxCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDialogButtonBoxCall44 call = reinterpret_cast<CuteQDialogButtonBoxCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQDialogButtonBoxCall45 call = reinterpret_cast<CuteQDialogButtonBoxCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDialogButtonBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDialogButtonBox10metaObjectEv(
    const QDialogButtonBox *self) {
  return self->metaObject();
}

//  QString QDialogButtonBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDialogButtonBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDialogButtonBox::tr(s, c, n));
}

//  QDialogButtonBox::QDialogButtonBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQDialogButtonBox(parent);
}

//  QDialogButtonBox::QDialogButtonBox(Qt::Orientation orientation, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new CuteQDialogButtonBox(orientation, parent);
}

//  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEP7QWidget(
    int buttons,
    QWidget *parent) {
  return new CuteQDialogButtonBox(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons),
      parent);
}

//  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons,
//      Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDialogButtonBox *ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEN2Qt11OrientationEP7QWidget(
    int buttons,
    Qt::Orientation orientation,
    QWidget *parent) {
  return new CuteQDialogButtonBox(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons),
      orientation,
      parent);
}

//  QDialogButtonBox::~QDialogButtonBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBoxD1Ev(QDialogButtonBox *self) {
  delete self;
}

//  void QDialogButtonBox::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox14setOrientationEN2Qt11OrientationE(
    QDialogButtonBox *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QDialogButtonBox::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK16QDialogButtonBox11orientationEv(
    const QDialogButtonBox *self) {
  return self->orientation();
}

//  void QDialogButtonBox::addButton(QAbstractButton *button, ButtonRole
//      role)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox9addButtonEP15QAbstractButtonNS_10ButtonRoleE(
    QDialogButtonBox *self,
    QAbstractButton *button,
    QDialogButtonBox::ButtonRole role) {
  self->addButton(button, role);
}

//  QPushButton *QDialogButtonBox::addButton(const QString &text, ButtonRole
//      role)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN16QDialogButtonBox9addButtonERK7QStringNS_10ButtonRoleE(
    QDialogButtonBox *self,
    const QString *text,
    QDialogButtonBox::ButtonRole role) {
  return self->addButton(*text, role);
}

//  QPushButton *QDialogButtonBox::addButton(StandardButton button)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN16QDialogButtonBox9addButtonENS_14StandardButtonE(
    QDialogButtonBox *self,
    QDialogButtonBox::StandardButton button) {
  return self->addButton(button);
}

//  void QDialogButtonBox::removeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox12removeButtonEP15QAbstractButton(
    QDialogButtonBox *self,
    QAbstractButton *button) {
  self->removeButton(button);
}

//  void QDialogButtonBox::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox5clearEv(QDialogButtonBox *self) {
  self->clear();
}

//  QList<QAbstractButton *> QDialogButtonBox::buttons() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK16QDialogButtonBox7buttonsEv(
    const QDialogButtonBox *self) {
  return new QList<QAbstractButton *>(self->buttons());
}

//  ButtonRole QDialogButtonBox::buttonRole(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QDialogButtonBox::ButtonRole ritual_ZNK16QDialogButtonBox10buttonRoleEP15QAbstractButton(
    const QDialogButtonBox *self,
    QAbstractButton *button) {
  return self->buttonRole(button);
}

//  void QDialogButtonBox::setStandardButtons(StandardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox18setStandardButtonsE6QFlagsINS_14StandardButtonEE(
    QDialogButtonBox *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QDialogButtonBox::StandardButton>::fromInt(buttons));
}

//  StandardButtons QDialogButtonBox::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDialogButtonBox15standardButtonsEv(
    const QDialogButtonBox *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  StandardButton QDialogButtonBox::standardButton(QAbstractButton *button)
//      const
extern "C" Q_DECL_EXPORT
QDialogButtonBox::StandardButton ritual_ZNK16QDialogButtonBox14standardButtonEP15QAbstractButton(
    const QDialogButtonBox *self,
    QAbstractButton *button) {
  return self->standardButton(button);
}

//  QPushButton *QDialogButtonBox::button(StandardButton which) const
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZNK16QDialogButtonBox6buttonENS_14StandardButtonE(
    const QDialogButtonBox *self,
    QDialogButtonBox::StandardButton which) {
  return self->button(which);
}

//  void QDialogButtonBox::setCenterButtons(bool center)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox16setCenterButtonsEb(
    QDialogButtonBox *self,
    bool center) {
  self->setCenterButtons(center);
}

//  bool QDialogButtonBox::centerButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDialogButtonBox13centerButtonsEv(
    const QDialogButtonBox *self) {
  return self->centerButtons();
}

//  QString QDialogButtonBox::standardButtonText(StandardButton button)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDialogButtonBox18standardButtonTextENS_14StandardButtonE(
    QDialogButtonBox::StandardButton button) {
  return new QString(QDialogButtonBox::standardButtonText(button));
}

//  QKeySequence QDialogButtonBox::standardButtonShortcut(StandardButton
//      button)
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZN16QDialogButtonBox22standardButtonShortcutENS_14StandardButtonE(
    QDialogButtonBox::StandardButton button) {
  return new QKeySequence(QDialogButtonBox::standardButtonShortcut(button));
}

//  void QDialogButtonBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDialogButtonBox11changeEventEP6QEvent(
    QDialogButtonBox *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  bool QDialogButtonBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDialogButtonBox5eventEP6QEvent(
    QDialogButtonBox *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQDialogButtonBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDialogButtonBox(
    QDialogButtonBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDialogButtonBox *>(self)->take(key, call);
}

//  void QDialogButtonBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QDialogButtonBox11changeEventEP6QEvent(
    QDialogButtonBox *self,
    QEvent *event) {
  static_cast<OwnQDialogButtonBox *>(self)->OwnQDialogButtonBox::changeEvent(
      event);
}

//  bool QDialogButtonBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QDialogButtonBox5eventEP6QEvent(
    QDialogButtonBox *self,
    QEvent *event) {
  return static_cast<OwnQDialogButtonBox *>(self)->OwnQDialogButtonBox::event(
      event);
}
