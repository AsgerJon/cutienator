//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qwizard.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWizard may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWizard : QWizard {
  using QWizard::event;
  using QWizard::resizeEvent;
  using QWizard::paintEvent;
  using QWizard::done;
  using QWizard::initializePage;
  using QWizard::cleanupPage;
};

//  A QWizard that Python can take functions over in. Every QWizard
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQWizardCall0)(const void *, int *);
typedef int (*CuteQWizardCall1)(const void *, int *);
typedef void (*CuteQWizardCall2)(const void *, bool, int *);
typedef const QSize * (*CuteQWizardCall3)(const void *, int *);
typedef bool (*CuteQWizardCall4)(const void *, QEvent *, int *);
typedef void (*CuteQWizardCall5)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWizardCall6)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWizardCall7)(const void *, int, int *);
typedef void (*CuteQWizardCall8)(const void *, int, int *);
typedef void (*CuteQWizardCall9)(const void *, int, int *);
typedef const QSize * (*CuteQWizardCall10)(const void *, int *);
typedef void (*CuteQWizardCall11)(const void *, int *);
typedef int (*CuteQWizardCall12)(const void *, int *);
typedef void (*CuteQWizardCall13)(const void *, int *);
typedef void (*CuteQWizardCall14)(const void *, int *);
typedef void (*CuteQWizardCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWizardCall16)(const void *, QCloseEvent *, int *);
typedef void (*CuteQWizardCall17)(const void *, QShowEvent *, int *);
typedef void (*CuteQWizardCall18)(const void *, QContextMenuEvent *, int *);
typedef bool (*CuteQWizardCall19)(const void *, QObject *, QEvent *, int *);
typedef int (*CuteQWizardCall20)(const void *, int *);
typedef int (*CuteQWizardCall21)(const void *, int, int *);
typedef bool (*CuteQWizardCall22)(const void *, int *);
typedef void * (*CuteQWizardCall23)(const void *, int *);
typedef void (*CuteQWizardCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardCall28)(const void *, QWheelEvent *, int *);
typedef void (*CuteQWizardCall29)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWizardCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWizardCall31)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWizardCall32)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWizardCall33)(const void *, QEvent *, int *);
typedef void (*CuteQWizardCall34)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWizardCall35)(const void *, QTabletEvent *, int *);
typedef void (*CuteQWizardCall36)(const void *, QActionEvent *, int *);
typedef void (*CuteQWizardCall37)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQWizardCall38)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQWizardCall39)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQWizardCall40)(const void *, QDropEvent *, int *);
typedef void (*CuteQWizardCall41)(const void *, QHideEvent *, int *);
typedef void (*CuteQWizardCall42)(const void *, QEvent *, int *);
typedef int (*CuteQWizardCall43)(const void *, int, int *);
typedef void (*CuteQWizardCall44)(const void *, QPainter *, int *);
typedef void * (*CuteQWizardCall45)(const void *, QPoint *, int *);
typedef void * (*CuteQWizardCall46)(const void *, int *);
typedef void (*CuteQWizardCall47)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWizardCall48)(const void *, int, int *);
typedef bool (*CuteQWizardCall49)(const void *, bool, int *);
typedef void (*CuteQWizardCall50)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWizardCall51)(const void *, QChildEvent *, int *);
typedef void (*CuteQWizardCall52)(const void *, QEvent *, int *);
typedef void (*CuteQWizardCall53)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWizardCall54)(const void *, const QMetaMethod *, int *);
class CuteQWizard : public QWizard {
public:
  using QWizard::QWizard;
  void *taken[55] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWizard19validateCurrentPageEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWizard6nextIdEv")) {
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
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWizard14initializePageEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWizard11cleanupPageEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
    return false;
  }

  //  bool QWizard::validateCurrentPage()
  bool validateCurrentPage() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWizardCall0 call = reinterpret_cast<CuteQWizardCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWizard::validateCurrentPage();
  }

  //  int QWizard::nextId() const
  int nextId() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWizardCall1 call = reinterpret_cast<CuteQWizardCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWizard::nextId();
  }

  //  void QWizard::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWizardCall2 call = reinterpret_cast<CuteQWizardCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWizard::setVisible(visible);
  }

  //  QSize QWizard::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWizardCall3 call = reinterpret_cast<CuteQWizardCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWizard::sizeHint();
  }

  //  bool QWizard::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWizardCall4 call = reinterpret_cast<CuteQWizardCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWizard::event(event);
  }

  //  void QWizard::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWizardCall5 call = reinterpret_cast<CuteQWizardCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWizard::resizeEvent(event);
  }

  //  void QWizard::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWizardCall6 call = reinterpret_cast<CuteQWizardCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWizard::paintEvent(event);
  }

  //  void QWizard::done(int result)
  void done(int result) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWizardCall7 call = reinterpret_cast<CuteQWizardCall7>(taken[7]);
      call(this, result, &handled);
      if (handled) return;
    }
    QWizard::done(result);
  }

  //  void QWizard::initializePage(int id)
  void initializePage(int id) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWizardCall8 call = reinterpret_cast<CuteQWizardCall8>(taken[8]);
      call(this, id, &handled);
      if (handled) return;
    }
    QWizard::initializePage(id);
  }

  //  void QWizard::cleanupPage(int id)
  void cleanupPage(int id) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWizardCall9 call = reinterpret_cast<CuteQWizardCall9>(taken[9]);
      call(this, id, &handled);
      if (handled) return;
    }
    QWizard::cleanupPage(id);
  }

  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWizardCall10 call = reinterpret_cast<CuteQWizardCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }

  //  void QDialog::open()
  void open() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWizardCall11 call = reinterpret_cast<CuteQWizardCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }

  //  int QDialog::exec()
  int exec() override {
    if (taken[12]) {
      int handled = 0;
      CuteQWizardCall12 call = reinterpret_cast<CuteQWizardCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }

  //  void QDialog::accept()
  void accept() override {
    if (taken[13]) {
      int handled = 0;
      CuteQWizardCall13 call = reinterpret_cast<CuteQWizardCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }

  //  void QDialog::reject()
  void reject() override {
    if (taken[14]) {
      int handled = 0;
      CuteQWizardCall14 call = reinterpret_cast<CuteQWizardCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }

  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWizardCall15 call = reinterpret_cast<CuteQWizardCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }

  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWizardCall16 call = reinterpret_cast<CuteQWizardCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }

  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWizardCall17 call = reinterpret_cast<CuteQWizardCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }

  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWizardCall18 call = reinterpret_cast<CuteQWizardCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }

  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWizardCall19 call = reinterpret_cast<CuteQWizardCall19>(taken[19]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQWizardCall20 call = reinterpret_cast<CuteQWizardCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQWizardCall21 call = reinterpret_cast<CuteQWizardCall21>(taken[21]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQWizardCall22 call = reinterpret_cast<CuteQWizardCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQWizardCall23 call = reinterpret_cast<CuteQWizardCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWizardCall24 call = reinterpret_cast<CuteQWizardCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWizardCall25 call = reinterpret_cast<CuteQWizardCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWizardCall26 call = reinterpret_cast<CuteQWizardCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWizardCall27 call = reinterpret_cast<CuteQWizardCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWizardCall28 call = reinterpret_cast<CuteQWizardCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWizardCall29 call = reinterpret_cast<CuteQWizardCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWizardCall30 call = reinterpret_cast<CuteQWizardCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWizardCall31 call = reinterpret_cast<CuteQWizardCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWizardCall32 call = reinterpret_cast<CuteQWizardCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWizardCall33 call = reinterpret_cast<CuteQWizardCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQWizardCall34 call = reinterpret_cast<CuteQWizardCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQWizardCall35 call = reinterpret_cast<CuteQWizardCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQWizardCall36 call = reinterpret_cast<CuteQWizardCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQWizardCall37 call = reinterpret_cast<CuteQWizardCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQWizardCall38 call = reinterpret_cast<CuteQWizardCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQWizardCall39 call = reinterpret_cast<CuteQWizardCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQWizardCall40 call = reinterpret_cast<CuteQWizardCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQWizardCall41 call = reinterpret_cast<CuteQWizardCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQWizardCall42 call = reinterpret_cast<CuteQWizardCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQWizardCall43 call = reinterpret_cast<CuteQWizardCall43>(taken[43]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQWizardCall44 call = reinterpret_cast<CuteQWizardCall44>(taken[44]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQWizardCall45 call = reinterpret_cast<CuteQWizardCall45>(taken[45]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQWizardCall46 call = reinterpret_cast<CuteQWizardCall46>(taken[46]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQWizardCall47 call = reinterpret_cast<CuteQWizardCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQWizardCall48 call = reinterpret_cast<CuteQWizardCall48>(taken[48]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[49]) {
      int handled = 0;
      CuteQWizardCall49 call = reinterpret_cast<CuteQWizardCall49>(taken[49]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQWizardCall50 call = reinterpret_cast<CuteQWizardCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQWizardCall51 call = reinterpret_cast<CuteQWizardCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQWizardCall52 call = reinterpret_cast<CuteQWizardCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteQWizardCall53 call = reinterpret_cast<CuteQWizardCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQWizardCall54 call = reinterpret_cast<CuteQWizardCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWizard::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QWizard10metaObjectEv(const QWizard *self) {
  return self->metaObject();
}

//  QString QWizard::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QWizard2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWizard::tr(s, c, n));
}

//  QWizard::QWizard(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QWizard *ritual_ZN7QWizardC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQWizard(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QWizard::~QWizard()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizardD1Ev(QWizard *self) {
  delete self;
}

//  int QWizard::addPage(QWizardPage *page)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QWizard7addPageEP11QWizardPage(
    QWizard *self,
    QWizardPage *page) {
  return self->addPage(page);
}

//  void QWizard::setPage(int id, QWizardPage *page)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard7setPageEiP11QWizardPage(
    QWizard *self,
    int id,
    QWizardPage *page) {
  self->setPage(id, page);
}

//  void QWizard::removePage(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10removePageEi(QWizard *self, int id) {
  self->removePage(id);
}

//  QWizardPage *QWizard::page(int id) const
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZNK7QWizard4pageEi(const QWizard *self, int id) {
  return self->page(id);
}

//  bool QWizard::hasVisitedPage(int id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWizard14hasVisitedPageEi(const QWizard *self, int id) {
  return self->hasVisitedPage(id);
}

//  void QWizard::setStartId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setStartIdEi(QWizard *self, int id) {
  self->setStartId(id);
}

//  int QWizard::startId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard7startIdEv(const QWizard *self) {
  return self->startId();
}

//  QWizardPage *QWizard::currentPage() const
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZNK7QWizard11currentPageEv(const QWizard *self) {
  return self->currentPage();
}

//  int QWizard::currentId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard9currentIdEv(const QWizard *self) {
  return self->currentId();
}

//  bool QWizard::validateCurrentPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWizard19validateCurrentPageEv(QWizard *self) {
  return self->validateCurrentPage();
}

//  int QWizard::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard6nextIdEv(const QWizard *self) {
  return self->nextId();
}

//  void QWizard::setField(const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard8setFieldERK7QStringRK8QVariant(
    QWizard *self,
    const QString *name,
    const QVariant *value) {
  self->setField(*name, *value);
}

//  QVariant QWizard::field(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QWizard5fieldERK7QString(
    const QWizard *self,
    const QString *name) {
  return new QVariant(self->field(*name));
}

//  void QWizard::setWizardStyle(WizardStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard14setWizardStyleENS_11WizardStyleE(
    QWizard *self,
    QWizard::WizardStyle style) {
  self->setWizardStyle(style);
}

//  WizardStyle QWizard::wizardStyle() const
extern "C" Q_DECL_EXPORT
QWizard::WizardStyle ritual_ZNK7QWizard11wizardStyleEv(const QWizard *self) {
  return self->wizardStyle();
}

//  void QWizard::setOption(WizardOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setOptionENS_12WizardOptionEb(
    QWizard *self,
    QWizard::WizardOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QWizard::testOption(WizardOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWizard10testOptionENS_12WizardOptionE(
    const QWizard *self,
    QWizard::WizardOption option) {
  return self->testOption(option);
}

//  void QWizard::setOptions(WizardOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setOptionsE6QFlagsINS_12WizardOptionEE(
    QWizard *self,
    int options) {
  self->setOptions(QFlags<QWizard::WizardOption>::fromInt(options));
}

//  WizardOptions QWizard::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWizard7optionsEv(const QWizard *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QWizard::setButtonText(WizardButton which, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard13setButtonTextENS_12WizardButtonERK7QString(
    QWizard *self,
    QWizard::WizardButton which,
    const QString *text) {
  self->setButtonText(which, *text);
}

//  QString QWizard::buttonText(WizardButton which) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWizard10buttonTextENS_12WizardButtonE(
    const QWizard *self,
    QWizard::WizardButton which) {
  return new QString(self->buttonText(which));
}

//  void QWizard::setButton(WizardButton which, QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setButtonENS_12WizardButtonEP15QAbstractButton(
    QWizard *self,
    QWizard::WizardButton which,
    QAbstractButton *button) {
  self->setButton(which, button);
}

//  QAbstractButton *QWizard::button(WizardButton which) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK7QWizard6buttonENS_12WizardButtonE(
    const QWizard *self,
    QWizard::WizardButton which) {
  return self->button(which);
}

//  void QWizard::setTitleFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard14setTitleFormatEN2Qt10TextFormatE(
    QWizard *self,
    Qt::TextFormat format) {
  self->setTitleFormat(format);
}

//  Qt::TextFormat QWizard::titleFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK7QWizard11titleFormatEv(const QWizard *self) {
  return self->titleFormat();
}

//  void QWizard::setSubTitleFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard17setSubTitleFormatEN2Qt10TextFormatE(
    QWizard *self,
    Qt::TextFormat format) {
  self->setSubTitleFormat(format);
}

//  Qt::TextFormat QWizard::subTitleFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK7QWizard14subTitleFormatEv(const QWizard *self) {
  return self->subTitleFormat();
}

//  void QWizard::setPixmap(WizardPixmap which, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard9setPixmapENS_12WizardPixmapERK7QPixmap(
    QWizard *self,
    QWizard::WizardPixmap which,
    const QPixmap *pixmap) {
  self->setPixmap(which, *pixmap);
}

//  QPixmap QWizard::pixmap(WizardPixmap which) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK7QWizard6pixmapENS_12WizardPixmapE(
    const QWizard *self,
    QWizard::WizardPixmap which) {
  return new QPixmap(self->pixmap(which));
}

//  void QWizard::setSideWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard13setSideWidgetEP7QWidget(
    QWizard *self,
    QWidget *widget) {
  self->setSideWidget(widget);
}

//  QWidget *QWizard::sideWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QWizard10sideWidgetEv(const QWizard *self) {
  return self->sideWidget();
}

//  void QWizard::setDefaultProperty(const char *className, const char
//      *property, const char *changedSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard18setDefaultPropertyEPKcS1_S1_(
    QWizard *self,
    const char *className,
    const char *property,
    const char *changedSignal) {
  self->setDefaultProperty(className, property, changedSignal);
}

//  void QWizard::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10setVisibleEb(QWizard *self, bool visible) {
  self->setVisible(visible);
}

//  QSize QWizard::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWizard8sizeHintEv(const QWizard *self) {
  return new QSize(self->sizeHint());
}

//  void QWizard::back()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard4backEv(QWizard *self) {
  self->back();
}

//  void QWizard::next()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard4nextEv(QWizard *self) {
  self->next();
}

//  void QWizard::setCurrentId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard12setCurrentIdEi(QWizard *self, int id) {
  self->setCurrentId(id);
}

//  void QWizard::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard7restartEv(QWizard *self) {
  self->restart();
}

//  bool QWizard::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWizard5eventEP6QEvent(QWizard *self, QEvent *event) {
  return self->event(event);
}

//  void QWizard::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard11resizeEventEP12QResizeEvent(
    QWizard *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QWizard::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard10paintEventEP11QPaintEvent(
    QWizard *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QWizard::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard4doneEi(QWizard *self, int result) {
  self->done(result);
}

//  void QWizard::initializePage(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard14initializePageEi(QWizard *self, int id) {
  self->initializePage(id);
}

//  void QWizard::cleanupPage(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWizard11cleanupPageEi(QWizard *self, int id) {
  self->cleanupPage(id);
}

//  a Python function taken by a CuteQWizard, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWizard(QWizard *self, const char *key, void *call) {
  return static_cast<CuteQWizard *>(self)->take(key, call);
}

//  bool QWizard::validateCurrentPage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QWizard19validateCurrentPageEv(QWizard *self) {
  return self->QWizard::validateCurrentPage();
}

//  int QWizard::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK7QWizard6nextIdEv(const QWizard *self) {
  return self->QWizard::nextId();
}

//  void QWizard::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard10setVisibleEb(QWizard *self, bool visible) {
  self->QWizard::setVisible(visible);
}

//  QSize QWizard::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QWizard8sizeHintEv(const QWizard *self) {
  return new QSize(self->QWizard::sizeHint());
}

//  bool QWizard::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QWizard5eventEP6QEvent(QWizard *self, QEvent *event) {
  return static_cast<OwnQWizard *>(self)->OwnQWizard::event(event);
}

//  void QWizard::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard11resizeEventEP12QResizeEvent(
    QWizard *self,
    QResizeEvent *event) {
  static_cast<OwnQWizard *>(self)->OwnQWizard::resizeEvent(event);
}

//  void QWizard::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard10paintEventEP11QPaintEvent(
    QWizard *self,
    QPaintEvent *event) {
  static_cast<OwnQWizard *>(self)->OwnQWizard::paintEvent(event);
}

//  void QWizard::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard4doneEi(QWizard *self, int result) {
  static_cast<OwnQWizard *>(self)->OwnQWizard::done(result);
}

//  void QWizard::initializePage(int id)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard14initializePageEi(QWizard *self, int id) {
  static_cast<OwnQWizard *>(self)->OwnQWizard::initializePage(id);
}

//  void QWizard::cleanupPage(int id)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWizard11cleanupPageEi(QWizard *self, int id) {
  static_cast<OwnQWizard *>(self)->OwnQWizard::cleanupPage(id);
}
