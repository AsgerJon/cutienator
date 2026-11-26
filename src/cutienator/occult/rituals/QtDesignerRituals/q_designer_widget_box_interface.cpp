//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractwidgetbox.h>
#include <QtCore/qstring.h>
#include <QtDesigner/abstractdnditem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerWidgetBoxInterface that Python can take functions over in. Every QDesignerWidgetBoxInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerWidgetBoxInterfaceCall0)(const void *, int *);
typedef const QDesignerWidgetBoxInterface::Category * (*CuteQDesignerWidgetBoxInterfaceCall1)(const void *, int, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall2)(const void *, const QDesignerWidgetBoxInterface::Category *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall3)(const void *, int, int *);
typedef int (*CuteQDesignerWidgetBoxInterfaceCall4)(const void *, int, int *);
typedef const QDesignerWidgetBoxInterface::Widget * (*CuteQDesignerWidgetBoxInterfaceCall5)(const void *, int, int, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall6)(const void *, int, const QDesignerWidgetBoxInterface::Widget *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall7)(const void *, int, int, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall8)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerWidgetBoxInterfaceCall9)(const void *, int *);
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall10)(const void *, int *);
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall11)(const void *, int *);
typedef int (*CuteQDesignerWidgetBoxInterfaceCall12)(const void *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall13)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerWidgetBoxInterfaceCall14)(const void *, int *);
typedef const QSize * (*CuteQDesignerWidgetBoxInterfaceCall15)(const void *, int *);
typedef int (*CuteQDesignerWidgetBoxInterfaceCall16)(const void *, int, int *);
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall17)(const void *, int *);
typedef void * (*CuteQDesignerWidgetBoxInterfaceCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall30)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall31)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall32)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall33)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall34)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall35)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall36)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall37)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall38)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall39)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall40)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall41)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall42)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall43)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall44)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerWidgetBoxInterfaceCall45)(const void *, int, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall46)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerWidgetBoxInterfaceCall47)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerWidgetBoxInterfaceCall48)(const void *, int *);
typedef void (*CuteQDesignerWidgetBoxInterfaceCall49)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerWidgetBoxInterfaceCall50)(const void *, int, int *);
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall51)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerWidgetBoxInterfaceCall52)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall53)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall54)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall55)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerWidgetBoxInterfaceCall57)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerWidgetBoxInterface : public QDesignerWidgetBoxInterface {
public:
  using QDesignerWidgetBoxInterface::QDesignerWidgetBoxInterface;
  void *taken[58] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QDesignerWidgetBoxInterface13categoryCountEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerWidgetBoxInterface8categoryEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface11addCategoryERKNS_8CategoryE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface14removeCategoryEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerWidgetBoxInterface11widgetCountEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerWidgetBoxInterface6widgetEii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface9addWidgetEiRKNS_6WidgetE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface12removeWidgetEii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface11setFileNameERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerWidgetBoxInterface8fileNameEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface4loadEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerWidgetBoxInterface4saveEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[51] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[57] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QDesignerWidgetBoxInterface::categoryCount() const
  int categoryCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall0 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Category QDesignerWidgetBoxInterface::category(int cat_idx) const
  QDesignerWidgetBoxInterface::Category category(
      int cat_idx) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall1 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall1>(taken[1]);
      const QDesignerWidgetBoxInterface::Category * given = call(this, cat_idx, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerWidgetBoxInterface::addCategory(const Category &cat)
  void addCategory(
      const QDesignerWidgetBoxInterface::Category &cat) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall2 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall2>(taken[2]);
      call(this, &cat, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerWidgetBoxInterface::removeCategory(int cat_idx)
  void removeCategory(int cat_idx) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall3 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall3>(taken[3]);
      call(this, cat_idx, &handled);
      if (handled) return;
    }
  }

  //  int QDesignerWidgetBoxInterface::widgetCount(int cat_idx) const
  int widgetCount(int cat_idx) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall4 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall4>(taken[4]);
      int given = call(this, cat_idx, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Widget QDesignerWidgetBoxInterface::widget(int cat_idx, int wgt_idx)
  //      const
  QDesignerWidgetBoxInterface::Widget widget(
      int cat_idx,
      int wgt_idx) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall5 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall5>(taken[5]);
      const QDesignerWidgetBoxInterface::Widget * given = call(this, cat_idx, wgt_idx, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerWidgetBoxInterface::addWidget(int cat_idx, const Widget
  //      &wgt)
  void addWidget(
      int cat_idx,
      const QDesignerWidgetBoxInterface::Widget &wgt) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall6 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall6>(taken[6]);
      call(this, cat_idx, &wgt, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerWidgetBoxInterface::removeWidget(int cat_idx, int
  //      wgt_idx)
  void removeWidget(int cat_idx, int wgt_idx) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall7 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall7>(taken[7]);
      call(this, cat_idx, wgt_idx, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerWidgetBoxInterface::setFileName(const QString
  //      &file_name)
  void setFileName(const QString &file_name) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall8 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall8>(taken[8]);
      call(this, &file_name, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetBoxInterface::fileName() const
  QString fileName() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall9 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QDesignerWidgetBoxInterface::load()
  bool load() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall10 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerWidgetBoxInterface::save()
  bool save() override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall11 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall12 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall13 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall14 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall14>(taken[14]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall15 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall15>(taken[15]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall16 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall17 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall18 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall19 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall20 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall21 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall22 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall23 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall24 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall25 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall26 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall27 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall28 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall29 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall30 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall31 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall32 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall33 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall34 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall35 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall36 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall37 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall38 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall39 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall40 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall41 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall42 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall43 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall44 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall45 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall45>(taken[45]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall46 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall46>(taken[46]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall47 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall47>(taken[47]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[48]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall48 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall48>(taken[48]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall49 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[50]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall50 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall50>(taken[50]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[51]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall51 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall51>(taken[51]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall52 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall52>(taken[52]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall53 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall54 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall55 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[56]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall56 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[57]) {
      int handled = 0;
      CuteQDesignerWidgetBoxInterfaceCall57 call = reinterpret_cast<CuteQDesignerWidgetBoxInterfaceCall57>(taken[57]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerWidgetBoxInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDesignerWidgetBoxInterface10metaObjectEv(
    const QDesignerWidgetBoxInterface *self) {
  return self->metaObject();
}

//  void *QDesignerWidgetBoxInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDesignerWidgetBoxInterface11qt_metacastEPKc(
    QDesignerWidgetBoxInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerWidgetBoxInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDesignerWidgetBoxInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerWidgetBoxInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerWidgetBoxInterface::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDesignerWidgetBoxInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerWidgetBoxInterface::tr(s, c, n));
}

//  QDesignerWidgetBoxInterface::~QDesignerWidgetBoxInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterfaceD1Ev(
    QDesignerWidgetBoxInterface *self) {
  delete self;
}

//  int QDesignerWidgetBoxInterface::categoryCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDesignerWidgetBoxInterface13categoryCountEv(
    const QDesignerWidgetBoxInterface *self) {
  return self->categoryCount();
}

//  Category QDesignerWidgetBoxInterface::category(int cat_idx) const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Category *ritual_ZNK27QDesignerWidgetBoxInterface8categoryEi(
    const QDesignerWidgetBoxInterface *self,
    int cat_idx) {
  return new QDesignerWidgetBoxInterface::Category(self->category(cat_idx));
}

//  void QDesignerWidgetBoxInterface::addCategory(const Category &cat)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface11addCategoryERKNS_8CategoryE(
    QDesignerWidgetBoxInterface *self,
    const QDesignerWidgetBoxInterface::Category *cat) {
  self->addCategory(*cat);
}

//  void QDesignerWidgetBoxInterface::removeCategory(int cat_idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface14removeCategoryEi(
    QDesignerWidgetBoxInterface *self,
    int cat_idx) {
  self->removeCategory(cat_idx);
}

//  int QDesignerWidgetBoxInterface::widgetCount(int cat_idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDesignerWidgetBoxInterface11widgetCountEi(
    const QDesignerWidgetBoxInterface *self,
    int cat_idx) {
  return self->widgetCount(cat_idx);
}

//  Widget QDesignerWidgetBoxInterface::widget(int cat_idx, int wgt_idx)
//      const
extern "C" Q_DECL_EXPORT
QDesignerWidgetBoxInterface::Widget *ritual_ZNK27QDesignerWidgetBoxInterface6widgetEii(
    const QDesignerWidgetBoxInterface *self,
    int cat_idx,
    int wgt_idx) {
  return new QDesignerWidgetBoxInterface::Widget(
      self->widget(
          cat_idx,
          wgt_idx));
}

//  void QDesignerWidgetBoxInterface::addWidget(int cat_idx, const Widget
//      &wgt)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface9addWidgetEiRKNS_6WidgetE(
    QDesignerWidgetBoxInterface *self,
    int cat_idx,
    const QDesignerWidgetBoxInterface::Widget *wgt) {
  self->addWidget(cat_idx, *wgt);
}

//  void QDesignerWidgetBoxInterface::removeWidget(int cat_idx, int wgt_idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface12removeWidgetEii(
    QDesignerWidgetBoxInterface *self,
    int cat_idx,
    int wgt_idx) {
  self->removeWidget(cat_idx, wgt_idx);
}

//  int QDesignerWidgetBoxInterface::findOrInsertCategory(const QString
//      &categoryName)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDesignerWidgetBoxInterface20findOrInsertCategoryERK7QString(
    QDesignerWidgetBoxInterface *self,
    const QString *categoryName) {
  return self->findOrInsertCategory(*categoryName);
}

//  void QDesignerWidgetBoxInterface::dropWidgets(const
//      QList<QDesignerDnDItemInterface *> &item_list, const QPoint
//      &global_mouse_pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface11dropWidgetsERK5QListIP25QDesignerDnDItemInterfaceERK6QPoint(
    QDesignerWidgetBoxInterface *self,
    const QList<QDesignerDnDItemInterface *> *item_list,
    const QPoint *global_mouse_pos) {
  self->dropWidgets(*item_list, *global_mouse_pos);
}

//  void QDesignerWidgetBoxInterface::setFileName(const QString &file_name)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerWidgetBoxInterface11setFileNameERK7QString(
    QDesignerWidgetBoxInterface *self,
    const QString *file_name) {
  self->setFileName(*file_name);
}

//  QString QDesignerWidgetBoxInterface::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerWidgetBoxInterface8fileNameEv(
    const QDesignerWidgetBoxInterface *self) {
  return new QString(self->fileName());
}

//  bool QDesignerWidgetBoxInterface::load()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerWidgetBoxInterface4loadEv(
    QDesignerWidgetBoxInterface *self) {
  return self->load();
}

//  bool QDesignerWidgetBoxInterface::save()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerWidgetBoxInterface4saveEv(
    QDesignerWidgetBoxInterface *self) {
  return self->save();
}

//  a Python function taken by a CuteQDesignerWidgetBoxInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerWidgetBoxInterface(
    QDesignerWidgetBoxInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerWidgetBoxInterface *>(self)->take(key, call);
}
