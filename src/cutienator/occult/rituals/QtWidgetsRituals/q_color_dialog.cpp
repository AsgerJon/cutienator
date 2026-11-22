//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcolordialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcolordialog.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QColorDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQColorDialog : QColorDialog {
  using QColorDialog::changeEvent;
  using QColorDialog::done;
};

//  A QColorDialog that Python can take functions over in. Every QColorDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQColorDialogCall0)(const void *, bool, int *);
typedef void (*CuteQColorDialogCall1)(const void *, QEvent *, int *);
typedef void (*CuteQColorDialogCall2)(const void *, int, int *);
typedef const QSize * (*CuteQColorDialogCall3)(const void *, int *);
typedef const QSize * (*CuteQColorDialogCall4)(const void *, int *);
typedef void (*CuteQColorDialogCall5)(const void *, int *);
typedef int (*CuteQColorDialogCall6)(const void *, int *);
typedef void (*CuteQColorDialogCall7)(const void *, int *);
typedef void (*CuteQColorDialogCall8)(const void *, int *);
typedef void (*CuteQColorDialogCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColorDialogCall10)(const void *, QCloseEvent *, int *);
typedef void (*CuteQColorDialogCall11)(const void *, QShowEvent *, int *);
typedef void (*CuteQColorDialogCall12)(const void *, QResizeEvent *, int *);
typedef void (*CuteQColorDialogCall13)(const void *, QContextMenuEvent *, int *);
typedef bool (*CuteQColorDialogCall14)(const void *, QObject *, QEvent *, int *);
typedef int (*CuteQColorDialogCall15)(const void *, int *);
typedef int (*CuteQColorDialogCall16)(const void *, int, int *);
typedef bool (*CuteQColorDialogCall17)(const void *, int *);
typedef void * (*CuteQColorDialogCall18)(const void *, int *);
typedef bool (*CuteQColorDialogCall19)(const void *, QEvent *, int *);
typedef void (*CuteQColorDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColorDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColorDialogCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColorDialogCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColorDialogCall24)(const void *, QWheelEvent *, int *);
typedef void (*CuteQColorDialogCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColorDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColorDialogCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColorDialogCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQColorDialogCall29)(const void *, QEvent *, int *);
typedef void (*CuteQColorDialogCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQColorDialogCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQColorDialogCall32)(const void *, QTabletEvent *, int *);
typedef void (*CuteQColorDialogCall33)(const void *, QActionEvent *, int *);
typedef void (*CuteQColorDialogCall34)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQColorDialogCall35)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQColorDialogCall36)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQColorDialogCall37)(const void *, QDropEvent *, int *);
typedef void (*CuteQColorDialogCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQColorDialogCall39)(const void *, int, int *);
typedef void (*CuteQColorDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQColorDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQColorDialogCall42)(const void *, int *);
typedef void (*CuteQColorDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQColorDialogCall44)(const void *, int, int *);
typedef bool (*CuteQColorDialogCall45)(const void *, bool, int *);
typedef void (*CuteQColorDialogCall46)(const void *, QTimerEvent *, int *);
typedef void (*CuteQColorDialogCall47)(const void *, QChildEvent *, int *);
typedef void (*CuteQColorDialogCall48)(const void *, QEvent *, int *);
typedef void (*CuteQColorDialogCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQColorDialogCall50)(const void *, const QMetaMethod *, int *);
class CuteQColorDialog : public QColorDialog {
public:
  using QColorDialog::QColorDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
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
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    return false;
  }

  //  void QColorDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQColorDialogCall0 call = reinterpret_cast<CuteQColorDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QColorDialog::setVisible(visible);
  }

  //  void QColorDialog::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColorDialogCall1 call = reinterpret_cast<CuteQColorDialogCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColorDialog::changeEvent(event);
  }

  //  void QColorDialog::done(int result)
  void done(int result) override {
    if (taken[2]) {
      int handled = 0;
      CuteQColorDialogCall2 call = reinterpret_cast<CuteQColorDialogCall2>(taken[2]);
      call(this, result, &handled);
      if (handled) return;
    }
    QColorDialog::done(result);
  }

  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQColorDialogCall3 call = reinterpret_cast<CuteQColorDialogCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }

  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQColorDialogCall4 call = reinterpret_cast<CuteQColorDialogCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }

  //  void QDialog::open()
  void open() override {
    if (taken[5]) {
      int handled = 0;
      CuteQColorDialogCall5 call = reinterpret_cast<CuteQColorDialogCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }

  //  int QDialog::exec()
  int exec() override {
    if (taken[6]) {
      int handled = 0;
      CuteQColorDialogCall6 call = reinterpret_cast<CuteQColorDialogCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }

  //  void QDialog::accept()
  void accept() override {
    if (taken[7]) {
      int handled = 0;
      CuteQColorDialogCall7 call = reinterpret_cast<CuteQColorDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }

  //  void QDialog::reject()
  void reject() override {
    if (taken[8]) {
      int handled = 0;
      CuteQColorDialogCall8 call = reinterpret_cast<CuteQColorDialogCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }

  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQColorDialogCall9 call = reinterpret_cast<CuteQColorDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }

  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQColorDialogCall10 call = reinterpret_cast<CuteQColorDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }

  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQColorDialogCall11 call = reinterpret_cast<CuteQColorDialogCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }

  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQColorDialogCall12 call = reinterpret_cast<CuteQColorDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }

  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQColorDialogCall13 call = reinterpret_cast<CuteQColorDialogCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }

  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQColorDialogCall14 call = reinterpret_cast<CuteQColorDialogCall14>(taken[14]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQColorDialogCall15 call = reinterpret_cast<CuteQColorDialogCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQColorDialogCall16 call = reinterpret_cast<CuteQColorDialogCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQColorDialogCall17 call = reinterpret_cast<CuteQColorDialogCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQColorDialogCall18 call = reinterpret_cast<CuteQColorDialogCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQColorDialogCall19 call = reinterpret_cast<CuteQColorDialogCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQColorDialogCall20 call = reinterpret_cast<CuteQColorDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQColorDialogCall21 call = reinterpret_cast<CuteQColorDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQColorDialogCall22 call = reinterpret_cast<CuteQColorDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQColorDialogCall23 call = reinterpret_cast<CuteQColorDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQColorDialogCall24 call = reinterpret_cast<CuteQColorDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQColorDialogCall25 call = reinterpret_cast<CuteQColorDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQColorDialogCall26 call = reinterpret_cast<CuteQColorDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQColorDialogCall27 call = reinterpret_cast<CuteQColorDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQColorDialogCall28 call = reinterpret_cast<CuteQColorDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQColorDialogCall29 call = reinterpret_cast<CuteQColorDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQColorDialogCall30 call = reinterpret_cast<CuteQColorDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQColorDialogCall31 call = reinterpret_cast<CuteQColorDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQColorDialogCall32 call = reinterpret_cast<CuteQColorDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQColorDialogCall33 call = reinterpret_cast<CuteQColorDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQColorDialogCall34 call = reinterpret_cast<CuteQColorDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQColorDialogCall35 call = reinterpret_cast<CuteQColorDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQColorDialogCall36 call = reinterpret_cast<CuteQColorDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQColorDialogCall37 call = reinterpret_cast<CuteQColorDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQColorDialogCall38 call = reinterpret_cast<CuteQColorDialogCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQColorDialogCall39 call = reinterpret_cast<CuteQColorDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQColorDialogCall40 call = reinterpret_cast<CuteQColorDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQColorDialogCall41 call = reinterpret_cast<CuteQColorDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQColorDialogCall42 call = reinterpret_cast<CuteQColorDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQColorDialogCall43 call = reinterpret_cast<CuteQColorDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQColorDialogCall44 call = reinterpret_cast<CuteQColorDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQColorDialogCall45 call = reinterpret_cast<CuteQColorDialogCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQColorDialogCall46 call = reinterpret_cast<CuteQColorDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQColorDialogCall47 call = reinterpret_cast<CuteQColorDialogCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQColorDialogCall48 call = reinterpret_cast<CuteQColorDialogCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQColorDialogCall49 call = reinterpret_cast<CuteQColorDialogCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQColorDialogCall50 call = reinterpret_cast<CuteQColorDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QColorDialog10metaObjectEv(
    const QColorDialog *self) {
  return self->metaObject();
}

//  QString QColorDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QColorDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColorDialog::tr(s, c, n));
}

//  QColorDialog::QColorDialog(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColorDialog *ritual_ZN12QColorDialogC1EP7QWidget(QWidget *parent) {
  return new CuteQColorDialog(parent);
}

//  QColorDialog::QColorDialog(const QColor &initial, QWidget *parent)
extern "C" Q_DECL_EXPORT
QColorDialog *ritual_ZN12QColorDialogC1ERK6QColorP7QWidget(
    const QColor *initial,
    QWidget *parent) {
  return new CuteQColorDialog(*initial, parent);
}

//  QColorDialog::~QColorDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialogD1Ev(QColorDialog *self) {
  delete self;
}

//  void QColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog15setCurrentColorERK6QColor(
    QColorDialog *self,
    const QColor *color) {
  self->setCurrentColor(*color);
}

//  QColor QColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QColorDialog12currentColorEv(const QColorDialog *self) {
  return new QColor(self->currentColor());
}

//  QColor QColorDialog::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QColorDialog13selectedColorEv(const QColorDialog *self) {
  return new QColor(self->selectedColor());
}

//  void QColorDialog::setOption(ColorDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog9setOptionENS_17ColorDialogOptionEb(
    QColorDialog *self,
    QColorDialog::ColorDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QColorDialog::testOption(ColorDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QColorDialog10testOptionENS_17ColorDialogOptionE(
    const QColorDialog *self,
    QColorDialog::ColorDialogOption option) {
  return self->testOption(option);
}

//  void QColorDialog::setOptions(ColorDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog10setOptionsE6QFlagsINS_17ColorDialogOptionEE(
    QColorDialog *self,
    int options) {
  self->setOptions(
      QFlags<QColorDialog::ColorDialogOption>::fromInt(options));
}

//  ColorDialogOptions QColorDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QColorDialog7optionsEv(const QColorDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QColorDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog4openEP7QObjectPKc(
    QColorDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QColorDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog10setVisibleEb(
    QColorDialog *self,
    bool visible) {
  self->setVisible(visible);
}

//  QColor QColorDialog::getColor(const QColor &initial, QWidget *parent,
//      const QString &title, ColorDialogOptions options)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog8getColorERK6QColorP7QWidgetRK7QString6QFlagsINS_17ColorDialogOptionEE(
    const QColor *initial,
    QWidget *parent,
    const QString *title,
    int options) {
  return new QColor(
      QColorDialog::getColor(
          *initial,
          parent,
          *title,
          QFlags<QColorDialog::ColorDialogOption>::fromInt(options)));
}

//  int QColorDialog::customCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QColorDialog11customCountEv() {
  return QColorDialog::customCount();
}

//  QColor QColorDialog::customColor(int index)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog11customColorEi(int index) {
  return new QColor(QColorDialog::customColor(index));
}

//  void QColorDialog::setCustomColor(int index, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog14setCustomColorEi6QColor(
    int index,
    const QColor *color) {
  QColorDialog::setCustomColor(index, *color);
}

//  QColor QColorDialog::standardColor(int index)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN12QColorDialog13standardColorEi(int index) {
  return new QColor(QColorDialog::standardColor(index));
}

//  void QColorDialog::setStandardColor(int index, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QColorDialog16setStandardColorEi6QColor(
    int index,
    const QColor *color) {
  QColorDialog::setStandardColor(index, *color);
}

//  a Python function taken by a CuteQColorDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColorDialog(
    QColorDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColorDialog *>(self)->take(key, call);
}

//  void QColorDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QColorDialog10setVisibleEb(
    QColorDialog *self,
    bool visible) {
  self->QColorDialog::setVisible(visible);
}

//  void QColorDialog::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QColorDialog11changeEventEP6QEvent(
    QColorDialog *self,
    QEvent *event) {
  static_cast<OwnQColorDialog *>(self)->OwnQColorDialog::changeEvent(event);
}

//  void QColorDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QColorDialog4doneEi(QColorDialog *self, int result) {
  static_cast<OwnQColorDialog *>(self)->OwnQColorDialog::done(result);
}
