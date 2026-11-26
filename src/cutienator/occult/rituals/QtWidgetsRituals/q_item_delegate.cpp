//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/qitemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qvariant.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QItemDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQItemDelegate : QItemDelegate {
  using QItemDelegate::drawDisplay;
  using QItemDelegate::drawDecoration;
  using QItemDelegate::drawFocus;
  using QItemDelegate::drawCheck;
  using QItemDelegate::eventFilter;
  using QItemDelegate::editorEvent;
};

//  A QItemDelegate that Python can take functions over in. Every QItemDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQItemDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQItemDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall4)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall5)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall6)(const void *, QPainter *, const QStyleOptionViewItem *, const QRect *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall7)(const void *, QPainter *, const QStyleOptionViewItem *, const QRect *, const QPixmap *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall8)(const void *, QPainter *, const QStyleOptionViewItem *, const QRect *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall9)(const void *, QPainter *, const QStyleOptionViewItem *, const QRect *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQItemDelegateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQItemDelegateCall11)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQItemDelegateCall12)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQItemDelegateCall13)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemDelegateCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemDelegateCall15)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemDelegateCall16)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemDelegateCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemDelegateCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemDelegateCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemDelegate : public QItemDelegate {
public:
  using QItemDelegate::QItemDelegate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QString")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QPixmap")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOptionViewItemRK5QRect")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOptionViewItemRK5QRectN2Qt10CheckStateE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemDelegateCall0 call = reinterpret_cast<CuteQItemDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
    QItemDelegate::paint(painter, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QSize QItemDelegate::sizeHint(const QStyleOptionViewItem &option,
  //      const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemDelegateCall1 call = reinterpret_cast<CuteQItemDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return QItemDelegate::sizeHint(option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QWidget *QItemDelegate::createEditor(QWidget *parent, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  QWidget *createEditor(
      QWidget *parent,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQItemDelegateCall2 call = reinterpret_cast<CuteQItemDelegateCall2>(taken[2]);
      void * given = call(this, parent, &option, &index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QItemDelegate::createEditor(parent, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::setEditorData(QWidget *editor, const QModelIndex
  //      &index) const
  void setEditorData(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQItemDelegateCall3 call = reinterpret_cast<CuteQItemDelegateCall3>(taken[3]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QItemDelegate::setEditorData(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::setModelData(QWidget *editor, QAbstractItemModel
  //      *model, const QModelIndex &index) const
  void setModelData(
      QWidget *editor,
      QAbstractItemModel *model,
      const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQItemDelegateCall4 call = reinterpret_cast<CuteQItemDelegateCall4>(taken[4]);
      call(this, editor, model, &index, &handled);
      if (handled) return;
    }
    QItemDelegate::setModelData(editor, model, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::updateEditorGeometry(QWidget *editor, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void updateEditorGeometry(
      QWidget *editor,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQItemDelegateCall5 call = reinterpret_cast<CuteQItemDelegateCall5>(taken[5]);
      call(this, editor, &option, &index, &handled);
      if (handled) return;
    }
    QItemDelegate::updateEditorGeometry(editor, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::drawDisplay(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QRect &rect, const QString
  //      &text) const
  void drawDisplay(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QRect &rect,
      const QString &text) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQItemDelegateCall6 call = reinterpret_cast<CuteQItemDelegateCall6>(taken[6]);
      call(this, painter, &option, &rect, &text, &handled);
      if (handled) return;
    }
    QItemDelegate::drawDisplay(painter, option, rect, text);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::drawDecoration(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QRect &rect, const QPixmap
  //      &pixmap) const
  void drawDecoration(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QRect &rect,
      const QPixmap &pixmap) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQItemDelegateCall7 call = reinterpret_cast<CuteQItemDelegateCall7>(taken[7]);
      call(this, painter, &option, &rect, &pixmap, &handled);
      if (handled) return;
    }
    QItemDelegate::drawDecoration(painter, option, rect, pixmap);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::drawFocus(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QRect &rect) const
  void drawFocus(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QRect &rect) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQItemDelegateCall8 call = reinterpret_cast<CuteQItemDelegateCall8>(taken[8]);
      call(this, painter, &option, &rect, &handled);
      if (handled) return;
    }
    QItemDelegate::drawFocus(painter, option, rect);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QItemDelegate::drawCheck(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QRect &rect, Qt::CheckState
  //      state) const
  void drawCheck(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QRect &rect,
      Qt::CheckState state) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQItemDelegateCall9 call = reinterpret_cast<CuteQItemDelegateCall9>(taken[9]);
      call(this, painter, &option, &rect, static_cast<int>(state), &handled);
      if (handled) return;
    }
    QItemDelegate::drawCheck(painter, option, rect, state);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QItemDelegate::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQItemDelegateCall10 call = reinterpret_cast<CuteQItemDelegateCall10>(taken[10]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QItemDelegate::eventFilter(object, event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemviews)
  //  bool QItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
  //      *model, const QStyleOptionViewItem &option, const QModelIndex
  //      &index)
  bool editorEvent(
      QEvent *event,
      QAbstractItemModel *model,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQItemDelegateCall11 call = reinterpret_cast<CuteQItemDelegateCall11>(taken[11]);
      bool given = call(this, event, model, &option, &index, &handled);
      if (handled) return given;
    }
    return QItemDelegate::editorEvent(event, model, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
  //      QModelIndex &index) const
  void destroyEditor(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQItemDelegateCall12 call = reinterpret_cast<CuteQItemDelegateCall12>(taken[12]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::destroyEditor(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
  //      QAbstractItemView *view, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool helpEvent(
      QHelpEvent *event,
      QAbstractItemView *view,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[13]) {
      int handled = 0;
      CuteQItemDelegateCall13 call = reinterpret_cast<CuteQItemDelegateCall13>(taken[13]);
      bool given = call(this, event, view, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::helpEvent(event, view, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQItemDelegateCall14 call = reinterpret_cast<CuteQItemDelegateCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQItemDelegateCall15 call = reinterpret_cast<CuteQItemDelegateCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQItemDelegateCall16 call = reinterpret_cast<CuteQItemDelegateCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQItemDelegateCall17 call = reinterpret_cast<CuteQItemDelegateCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQItemDelegateCall18 call = reinterpret_cast<CuteQItemDelegateCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQItemDelegateCall19 call = reinterpret_cast<CuteQItemDelegateCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QItemDelegate10metaObjectEv(
    const QItemDelegate *self) {
  return self->metaObject();
}

//  void *QItemDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QItemDelegate11qt_metacastEPKc(
    QItemDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QItemDelegate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QItemDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QItemDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemDelegate::tr(s, c, n));
}

//  QItemDelegate::QItemDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QItemDelegate *ritual_ZN13QItemDelegateC1EP7QObject(QObject *parent) {
  return new CuteQItemDelegate(parent);
}

//  QItemDelegate::~QItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegateD1Ev(QItemDelegate *self) {
  delete self;
}

//  bool QItemDelegate::hasClipping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QItemDelegate11hasClippingEv(const QItemDelegate *self) {
  return self->hasClipping();
}

//  void QItemDelegate::setClipping(bool clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegate11setClippingEb(
    QItemDelegate *self,
    bool clip) {
  self->setClipping(clip);
}

//  void QItemDelegate::paint(QPainter *painter, const QStyleOptionViewItem
//      &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QItemDelegate::sizeHint(const QStyleOptionViewItem &option, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QItemDelegate::setEditorData(QWidget *editor, const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QItemDelegate::setModelData(QWidget *editor, QAbstractItemModel
//      *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  QItemEditorFactory *QItemDelegate::itemEditorFactory() const
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZNK13QItemDelegate17itemEditorFactoryEv(
    const QItemDelegate *self) {
  return self->itemEditorFactory();
}

//  void QItemDelegate::setItemEditorFactory(QItemEditorFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegate20setItemEditorFactoryEP18QItemEditorFactory(
    QItemDelegate *self,
    QItemEditorFactory *factory) {
  self->setItemEditorFactory(factory);
}

//  void QItemDelegate::drawDisplay(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, const QString &text)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QString(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    const QString *text) {
  self->drawDisplay(painter, *option, *rect, *text);
}

//  void QItemDelegate::drawDecoration(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, const QPixmap
//      &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QPixmap(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    const QPixmap *pixmap) {
  self->drawDecoration(painter, *option, *rect, *pixmap);
}

//  void QItemDelegate::drawFocus(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOptionViewItemRK5QRect(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect) {
  self->drawFocus(painter, *option, *rect);
}

//  void QItemDelegate::drawCheck(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, Qt::CheckState
//      state) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOptionViewItemRK5QRectN2Qt10CheckStateE(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    Qt::CheckState state) {
  self->drawCheck(painter, *option, *rect, state);
}

//  void QItemDelegate::drawBackground(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate14drawBackgroundEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->drawBackground(painter, *option, *index);
}

//  void QItemDelegate::doLayout(const QStyleOptionViewItem &option, QRect
//      *checkRect, QRect *iconRect, QRect *textRect, bool hint) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate8doLayoutERK20QStyleOptionViewItemP5QRectS4_S4_b(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    QRect *checkRect,
    QRect *iconRect,
    QRect *textRect,
    bool hint) {
  self->doLayout(*option, checkRect, iconRect, textRect, hint);
}

//  QRect QItemDelegate::rect(const QStyleOptionViewItem &option, const
//      QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QItemDelegate4rectERK20QStyleOptionViewItemRK11QModelIndexi(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index,
    int role) {
  return new QRect(self->rect(*option, *index, role));
}

//  bool QItemDelegate::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QItemDelegate11eventFilterEP7QObjectP6QEvent(
    QItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  bool QItemDelegate::editorEvent(QEvent *event, QAbstractItemModel *model,
//      const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->editorEvent(event, model, *option, *index);
}

//  QStyleOptionViewItem QItemDelegate::setOptions(const QModelIndex &index,
//      const QStyleOptionViewItem &option) const
extern "C" Q_DECL_EXPORT
QStyleOptionViewItem *ritual_ZNK13QItemDelegate10setOptionsERK11QModelIndexRK20QStyleOptionViewItem(
    const QItemDelegate *self,
    const QModelIndex *index,
    const QStyleOptionViewItem *option) {
  return new QStyleOptionViewItem(self->setOptions(*index, *option));
}

//  QPixmap QItemDelegate::decoration(const QStyleOptionViewItem &option,
//      const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK13QItemDelegate10decorationERK20QStyleOptionViewItemRK8QVariant(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QVariant *variant) {
  return new QPixmap(self->decoration(*option, *variant));
}

//  QPixmap QItemDelegate::selectedPixmap(const QPixmap &pixmap, const
//      QPalette &palette, bool enabled)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN13QItemDelegate14selectedPixmapERK7QPixmapRK8QPaletteb(
    const QPixmap *pixmap,
    const QPalette *palette,
    bool enabled) {
  return new QPixmap(
      QItemDelegate::selectedPixmap(
          *pixmap,
          *palette,
          enabled));
}

//  QRect QItemDelegate::doCheck(const QStyleOptionViewItem &option, const
//      QRect &bounding, const QVariant &variant) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QItemDelegate7doCheckERK20QStyleOptionViewItemRK5QRectRK8QVariant(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QRect *bounding,
    const QVariant *variant) {
  return new QRect(self->doCheck(*option, *bounding, *variant));
}

//  QRect QItemDelegate::textRectangle(QPainter *painter, const QRect &rect,
//      const QFont &font, const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QItemDelegate13textRectangleEP8QPainterRK5QRectRK5QFontRK7QString(
    const QItemDelegate *self,
    QPainter *painter,
    const QRect *rect,
    const QFont *font,
    const QString *text) {
  return new QRect(self->textRectangle(painter, *rect, *font, *text));
}

//  QItemDelegatePrivate *QItemDelegate::d_func()
extern "C" Q_DECL_EXPORT
QItemDelegatePrivate *ritual_ZN13QItemDelegate6d_funcEv(
    QItemDelegate *self) {
  return self->d_func();
}

//  const QItemDelegatePrivate *QItemDelegate::d_func() const
extern "C" Q_DECL_EXPORT
const QItemDelegatePrivate *ritual_ZNK13QItemDelegate6d_funcEv(
    const QItemDelegate *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQItemDelegate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemDelegate(
    QItemDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemDelegate *>(self)->take(key, call);
}

//  void QItemDelegate::paint(QPainter *painter, const QStyleOptionViewItem
//      &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QItemDelegate::paint(painter, *option, *index);
}

//  QSize QItemDelegate::sizeHint(const QStyleOptionViewItem &option, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->QItemDelegate::sizeHint(*option, *index));
}

//  QWidget *QItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->QItemDelegate::createEditor(parent, *option, *index);
}

//  void QItemDelegate::setEditorData(QWidget *editor, const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->QItemDelegate::setEditorData(editor, *index);
}

//  void QItemDelegate::setModelData(QWidget *editor, QAbstractItemModel
//      *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->QItemDelegate::setModelData(editor, model, *index);
}

//  void QItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QItemDelegate::updateEditorGeometry(editor, *option, *index);
}

//  void QItemDelegate::drawDisplay(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, const QString &text)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate11drawDisplayEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QString(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    const QString *text) {
  static_cast<const OwnQItemDelegate *>(self)->OwnQItemDelegate::drawDisplay(
      painter,
      *option,
      *rect,
      *text);
}

//  void QItemDelegate::drawDecoration(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, const QPixmap
//      &pixmap) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate14drawDecorationEP8QPainterRK20QStyleOptionViewItemRK5QRectRK7QPixmap(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    const QPixmap *pixmap) {
  static_cast<const OwnQItemDelegate *>(self)->OwnQItemDelegate::drawDecoration(
      painter,
      *option,
      *rect,
      *pixmap);
}

//  void QItemDelegate::drawFocus(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate9drawFocusEP8QPainterRK20QStyleOptionViewItemRK5QRect(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect) {
  static_cast<const OwnQItemDelegate *>(self)->OwnQItemDelegate::drawFocus(
      painter,
      *option,
      *rect);
}

//  void QItemDelegate::drawCheck(QPainter *painter, const
//      QStyleOptionViewItem &option, const QRect &rect, Qt::CheckState
//      state) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QItemDelegate9drawCheckEP8QPainterRK20QStyleOptionViewItemRK5QRectN2Qt10CheckStateE(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QRect *rect,
    Qt::CheckState state) {
  static_cast<const OwnQItemDelegate *>(self)->OwnQItemDelegate::drawCheck(
      painter,
      *option,
      *rect,
      state);
}

//  bool QItemDelegate::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QItemDelegate11eventFilterEP7QObjectP6QEvent(
    QItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQItemDelegate *>(self)->OwnQItemDelegate::eventFilter(
      object,
      event);
}

//  bool QItemDelegate::editorEvent(QEvent *event, QAbstractItemModel *model,
//      const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return static_cast<OwnQItemDelegate *>(self)->OwnQItemDelegate::editorEvent(
      event,
      model,
      *option,
      *index);
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
