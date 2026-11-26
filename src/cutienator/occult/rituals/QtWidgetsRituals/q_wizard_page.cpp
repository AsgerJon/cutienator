//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qwizard.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
#include <QtWidgets/QtWidgets>
#include <QtWidgets/qwizard.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWizardPage that Python can take functions over in. Every QWizardPage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wizard)
typedef void (*CuteQWizardPageCall0)(const void *, int *);
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
typedef void (*CuteQWizardPageCall1)(const void *, int *);
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
typedef bool (*CuteQWizardPageCall2)(const void *, int *);
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
typedef bool (*CuteQWizardPageCall3)(const void *, int *);
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
typedef int (*CuteQWizardPageCall4)(const void *, int *);
#endif  // QT_CONFIG(wizard)
typedef int (*CuteQWizardPageCall5)(const void *, int *);
typedef void (*CuteQWizardPageCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQWizardPageCall7)(const void *, int *);
typedef const QSize * (*CuteQWizardPageCall8)(const void *, int *);
typedef int (*CuteQWizardPageCall9)(const void *, int, int *);
typedef bool (*CuteQWizardPageCall10)(const void *, int *);
typedef void * (*CuteQWizardPageCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWizardPageCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardPageCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardPageCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWizardPageCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWizardPageCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWizardPageCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWizardPageCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWizardPageCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWizardPageCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWizardPageCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQWizardPageCall23)(const void *, QEvent *, int *);
typedef void (*CuteQWizardPageCall24)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWizardPageCall25)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWizardPageCall26)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWizardPageCall27)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQWizardPageCall28)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWizardPageCall29)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQWizardPageCall30)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWizardPageCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWizardPageCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWizardPageCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQWizardPageCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQWizardPageCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteQWizardPageCall36)(const void *, QHideEvent *, int *);
typedef void (*CuteQWizardPageCall37)(const void *, QEvent *, int *);
typedef int (*CuteQWizardPageCall38)(const void *, int, int *);
typedef void (*CuteQWizardPageCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQWizardPageCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQWizardPageCall41)(const void *, int *);
typedef void (*CuteQWizardPageCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQWizardPageCall43)(const void *, int, int *);
typedef bool (*CuteQWizardPageCall44)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWizardPageCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWizardPageCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWizardPage : public QWizardPage {
public:
  using QWizardPage::QWizardPage;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wizard)
    if (!std::strcmp(key, "_ZN11QWizardPage14initializePageEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
    if (!std::strcmp(key, "_ZN11QWizardPage11cleanupPageEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
    if (!std::strcmp(key, "_ZN11QWizardPage12validatePageEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
    if (!std::strcmp(key, "_ZNK11QWizardPage10isCompleteEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wizard)
#if QT_CONFIG(wizard)
    if (!std::strcmp(key, "_ZNK11QWizardPage6nextIdEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wizard)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[44] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wizard)
  //  void QWizardPage::initializePage()
  void initializePage() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWizardPageCall0 call = reinterpret_cast<CuteQWizardPageCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWizardPage::initializePage();
  }
#endif  // QT_CONFIG(wizard)

#if QT_CONFIG(wizard)
  //  void QWizardPage::cleanupPage()
  void cleanupPage() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWizardPageCall1 call = reinterpret_cast<CuteQWizardPageCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWizardPage::cleanupPage();
  }
#endif  // QT_CONFIG(wizard)

#if QT_CONFIG(wizard)
  //  bool QWizardPage::validatePage()
  bool validatePage() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWizardPageCall2 call = reinterpret_cast<CuteQWizardPageCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWizardPage::validatePage();
  }
#endif  // QT_CONFIG(wizard)

#if QT_CONFIG(wizard)
  //  bool QWizardPage::isComplete() const
  bool isComplete() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWizardPageCall3 call = reinterpret_cast<CuteQWizardPageCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWizardPage::isComplete();
  }
#endif  // QT_CONFIG(wizard)

#if QT_CONFIG(wizard)
  //  int QWizardPage::nextId() const
  int nextId() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWizardPageCall4 call = reinterpret_cast<CuteQWizardPageCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWizardPage::nextId();
  }
#endif  // QT_CONFIG(wizard)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWizardPageCall5 call = reinterpret_cast<CuteQWizardPageCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWizardPageCall6 call = reinterpret_cast<CuteQWizardPageCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWizardPageCall7 call = reinterpret_cast<CuteQWizardPageCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWizardPageCall8 call = reinterpret_cast<CuteQWizardPageCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWizardPageCall9 call = reinterpret_cast<CuteQWizardPageCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWizardPageCall10 call = reinterpret_cast<CuteQWizardPageCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWizardPageCall11 call = reinterpret_cast<CuteQWizardPageCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWizardPageCall12 call = reinterpret_cast<CuteQWizardPageCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWizardPageCall13 call = reinterpret_cast<CuteQWizardPageCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWizardPageCall14 call = reinterpret_cast<CuteQWizardPageCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWizardPageCall15 call = reinterpret_cast<CuteQWizardPageCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWizardPageCall16 call = reinterpret_cast<CuteQWizardPageCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWizardPageCall17 call = reinterpret_cast<CuteQWizardPageCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWizardPageCall18 call = reinterpret_cast<CuteQWizardPageCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWizardPageCall19 call = reinterpret_cast<CuteQWizardPageCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWizardPageCall20 call = reinterpret_cast<CuteQWizardPageCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWizardPageCall21 call = reinterpret_cast<CuteQWizardPageCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWizardPageCall22 call = reinterpret_cast<CuteQWizardPageCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWizardPageCall23 call = reinterpret_cast<CuteQWizardPageCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWizardPageCall24 call = reinterpret_cast<CuteQWizardPageCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWizardPageCall25 call = reinterpret_cast<CuteQWizardPageCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWizardPageCall26 call = reinterpret_cast<CuteQWizardPageCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWizardPageCall27 call = reinterpret_cast<CuteQWizardPageCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWizardPageCall28 call = reinterpret_cast<CuteQWizardPageCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWizardPageCall29 call = reinterpret_cast<CuteQWizardPageCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWizardPageCall30 call = reinterpret_cast<CuteQWizardPageCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQWizardPageCall31 call = reinterpret_cast<CuteQWizardPageCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQWizardPageCall32 call = reinterpret_cast<CuteQWizardPageCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQWizardPageCall33 call = reinterpret_cast<CuteQWizardPageCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQWizardPageCall34 call = reinterpret_cast<CuteQWizardPageCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQWizardPageCall35 call = reinterpret_cast<CuteQWizardPageCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQWizardPageCall36 call = reinterpret_cast<CuteQWizardPageCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQWizardPageCall37 call = reinterpret_cast<CuteQWizardPageCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQWizardPageCall38 call = reinterpret_cast<CuteQWizardPageCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQWizardPageCall39 call = reinterpret_cast<CuteQWizardPageCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQWizardPageCall40 call = reinterpret_cast<CuteQWizardPageCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQWizardPageCall41 call = reinterpret_cast<CuteQWizardPageCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQWizardPageCall42 call = reinterpret_cast<CuteQWizardPageCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQWizardPageCall43 call = reinterpret_cast<CuteQWizardPageCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQWizardPageCall44 call = reinterpret_cast<CuteQWizardPageCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQWizardPageCall45 call = reinterpret_cast<CuteQWizardPageCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQWizardPageCall46 call = reinterpret_cast<CuteQWizardPageCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQWizardPageCall47 call = reinterpret_cast<CuteQWizardPageCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQWizardPageCall48 call = reinterpret_cast<CuteQWizardPageCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQWizardPageCall49 call = reinterpret_cast<CuteQWizardPageCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQWizardPageCall50 call = reinterpret_cast<CuteQWizardPageCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWizardPage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QWizardPage10metaObjectEv(
    const QWizardPage *self) {
  return self->metaObject();
}

//  void *QWizardPage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QWizardPage11qt_metacastEPKc(
    QWizardPage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWizardPage::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWizardPage11qt_metacallEN11QMetaObject4CallEiPPv(
    QWizardPage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWizardPage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QWizardPage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWizardPage::tr(s, c, n));
}

//  QWizardPage::QWizardPage(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWizardPage *ritual_ZN11QWizardPageC1EP7QWidget(QWidget *parent) {
  return new CuteQWizardPage(parent);
}

//  QWizardPage::~QWizardPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPageD1Ev(QWizardPage *self) {
  delete self;
}

//  void QWizardPage::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage8setTitleERK7QString(
    QWizardPage *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QWizardPage::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage5titleEv(const QWizardPage *self) {
  return new QString(self->title());
}

//  void QWizardPage::setSubTitle(const QString &subTitle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage11setSubTitleERK7QString(
    QWizardPage *self,
    const QString *subTitle) {
  self->setSubTitle(*subTitle);
}

//  QString QWizardPage::subTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage8subTitleEv(const QWizardPage *self) {
  return new QString(self->subTitle());
}

//  void QWizardPage::setPixmap(QWizard::WizardPixmap which, const QPixmap
//      &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage9setPixmapEN7QWizard12WizardPixmapERK7QPixmap(
    QWizardPage *self,
    QWizard::WizardPixmap which,
    const QPixmap *pixmap) {
  self->setPixmap(which, *pixmap);
}

//  QPixmap QWizardPage::pixmap(QWizard::WizardPixmap which) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QWizardPage6pixmapEN7QWizard12WizardPixmapE(
    const QWizardPage *self,
    QWizard::WizardPixmap which) {
  return new QPixmap(self->pixmap(which));
}

//  void QWizardPage::setFinalPage(bool finalPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage12setFinalPageEb(
    QWizardPage *self,
    bool finalPage) {
  self->setFinalPage(finalPage);
}

//  bool QWizardPage::isFinalPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage11isFinalPageEv(const QWizardPage *self) {
  return self->isFinalPage();
}

//  void QWizardPage::setCommitPage(bool commitPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage13setCommitPageEb(
    QWizardPage *self,
    bool commitPage) {
  self->setCommitPage(commitPage);
}

//  bool QWizardPage::isCommitPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage12isCommitPageEv(const QWizardPage *self) {
  return self->isCommitPage();
}

//  void QWizardPage::setButtonText(QWizard::WizardButton which, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage13setButtonTextEN7QWizard12WizardButtonERK7QString(
    QWizardPage *self,
    QWizard::WizardButton which,
    const QString *text) {
  self->setButtonText(which, *text);
}

//  QString QWizardPage::buttonText(QWizard::WizardButton which) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QWizardPage10buttonTextEN7QWizard12WizardButtonE(
    const QWizardPage *self,
    QWizard::WizardButton which) {
  return new QString(self->buttonText(which));
}

//  void QWizardPage::initializePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage14initializePageEv(QWizardPage *self) {
  self->initializePage();
}

//  void QWizardPage::cleanupPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage11cleanupPageEv(QWizardPage *self) {
  self->cleanupPage();
}

//  bool QWizardPage::validatePage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QWizardPage12validatePageEv(QWizardPage *self) {
  return self->validatePage();
}

//  bool QWizardPage::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWizardPage10isCompleteEv(const QWizardPage *self) {
  return self->isComplete();
}

//  int QWizardPage::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWizardPage6nextIdEv(const QWizardPage *self) {
  return self->nextId();
}

//  void QWizardPage::completeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage15completeChangedEv(QWizardPage *self) {
  self->completeChanged();
}

//  void QWizardPage::setField(const QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage8setFieldERK7QStringRK8QVariant(
    QWizardPage *self,
    const QString *name,
    const QVariant *value) {
  self->setField(*name, *value);
}

//  QVariant QWizardPage::field(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QWizardPage5fieldERK7QString(
    const QWizardPage *self,
    const QString *name) {
  return new QVariant(self->field(*name));
}

//  void QWizardPage::registerField(const QString &name, QWidget *widget,
//      const char *property, const char *changedSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWizardPage13registerFieldERK7QStringP7QWidgetPKcS6_(
    QWizardPage *self,
    const QString *name,
    QWidget *widget,
    const char *property,
    const char *changedSignal) {
  self->registerField(*name, widget, property, changedSignal);
}

//  QWizard *QWizardPage::wizard() const
extern "C" Q_DECL_EXPORT
QWizard *ritual_ZNK11QWizardPage6wizardEv(const QWizardPage *self) {
  return self->wizard();
}

//  QWizardPagePrivate *QWizardPage::d_func()
extern "C" Q_DECL_EXPORT
QWizardPagePrivate *ritual_ZN11QWizardPage6d_funcEv(QWizardPage *self) {
  return self->d_func();
}

//  const QWizardPagePrivate *QWizardPage::d_func() const
extern "C" Q_DECL_EXPORT
const QWizardPagePrivate *ritual_ZNK11QWizardPage6d_funcEv(
    const QWizardPage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWizardPage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWizardPage(
    QWizardPage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWizardPage *>(self)->take(key, call);
}

//  void QWizardPage::initializePage()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QWizardPage14initializePageEv(QWizardPage *self) {
  self->QWizardPage::initializePage();
}

//  void QWizardPage::cleanupPage()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QWizardPage11cleanupPageEv(QWizardPage *self) {
  self->QWizardPage::cleanupPage();
}

//  bool QWizardPage::validatePage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QWizardPage12validatePageEv(QWizardPage *self) {
  return self->QWizardPage::validatePage();
}

//  bool QWizardPage::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWizardPage10isCompleteEv(const QWizardPage *self) {
  return self->QWizardPage::isComplete();
}

//  int QWizardPage::nextId() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QWizardPage6nextIdEv(const QWizardPage *self) {
  return self->QWizardPage::nextId();
}

#endif  // QT_CONFIG(wizard)
#endif  // QT_CONFIG(wizard)
