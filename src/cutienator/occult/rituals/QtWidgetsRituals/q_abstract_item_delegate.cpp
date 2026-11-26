//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractitemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A QAbstractItemDelegate that Python can take functions over in. Every QAbstractItemDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQAbstractItemDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAbstractItemDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemDelegateCall4)(const void *, QWidget *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemDelegateCall5)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemDelegateCall6)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemDelegateCall7)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemDelegateCall8)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemDelegateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemDelegateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemDelegateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemDelegateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemDelegateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemDelegateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemDelegateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractItemDelegate : public QAbstractItemDelegate {
public:
  using QAbstractItemDelegate::QAbstractItemDelegate;
  void *taken[16] = {};

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
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::paint(QPainter *painter, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  void paint(
      QPainter *painter,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall0 call = reinterpret_cast<CuteQAbstractItemDelegateCall0>(taken[0]);
      call(this, painter, &option, &index, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QSize QAbstractItemDelegate::sizeHint(const QStyleOptionViewItem
  //      &option, const QModelIndex &index) const
  QSize sizeHint(
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall1 call = reinterpret_cast<CuteQAbstractItemDelegateCall1>(taken[1]);
      const QSize * given = call(this, &option, &index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
  //      QStyleOptionViewItem &option, const QModelIndex &index) const
  QWidget *createEditor(
      QWidget *parent,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall2 call = reinterpret_cast<CuteQAbstractItemDelegateCall2>(taken[2]);
      void * given = call(this, parent, &option, &index, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAbstractItemDelegate::createEditor(parent, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
  //      QModelIndex &index) const
  void destroyEditor(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall3 call = reinterpret_cast<CuteQAbstractItemDelegateCall3>(taken[3]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::destroyEditor(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
  //      QModelIndex &index) const
  void setEditorData(
      QWidget *editor,
      const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall4 call = reinterpret_cast<CuteQAbstractItemDelegateCall4>(taken[4]);
      call(this, editor, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::setEditorData(editor, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::setModelData(QWidget *editor,
  //      QAbstractItemModel *model, const QModelIndex &index) const
  void setModelData(
      QWidget *editor,
      QAbstractItemModel *model,
      const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall5 call = reinterpret_cast<CuteQAbstractItemDelegateCall5>(taken[5]);
      call(this, editor, model, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::setModelData(editor, model, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor,
  //      const QStyleOptionViewItem &option, const QModelIndex &index)
  //      const
  void updateEditorGeometry(
      QWidget *editor,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall6 call = reinterpret_cast<CuteQAbstractItemDelegateCall6>(taken[6]);
      call(this, editor, &option, &index, &handled);
      if (handled) return;
    }
    QAbstractItemDelegate::updateEditorGeometry(editor, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemDelegate::editorEvent(QEvent *event,
  //      QAbstractItemModel *model, const QStyleOptionViewItem &option,
  //      const QModelIndex &index)
  bool editorEvent(
      QEvent *event,
      QAbstractItemModel *model,
      const QStyleOptionViewItem &option,
      const QModelIndex &index) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall7 call = reinterpret_cast<CuteQAbstractItemDelegateCall7>(taken[7]);
      bool given = call(this, event, model, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::editorEvent(event, model, option, index);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall8 call = reinterpret_cast<CuteQAbstractItemDelegateCall8>(taken[8]);
      bool given = call(this, event, view, &option, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemDelegate::helpEvent(event, view, option, index);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall9 call = reinterpret_cast<CuteQAbstractItemDelegateCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall10 call = reinterpret_cast<CuteQAbstractItemDelegateCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall11 call = reinterpret_cast<CuteQAbstractItemDelegateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall12 call = reinterpret_cast<CuteQAbstractItemDelegateCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall13 call = reinterpret_cast<CuteQAbstractItemDelegateCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall14 call = reinterpret_cast<CuteQAbstractItemDelegateCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractItemDelegateCall15 call = reinterpret_cast<CuteQAbstractItemDelegateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractItemDelegate10metaObjectEv(
    const QAbstractItemDelegate *self) {
  return self->metaObject();
}

//  void *QAbstractItemDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QAbstractItemDelegate11qt_metacastEPKc(
    QAbstractItemDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractItemDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QAbstractItemDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractItemDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemDelegate::tr(s, c, n));
}

//  QAbstractItemDelegate::QAbstractItemDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZN21QAbstractItemDelegateC1EP7QObject(
    QObject *parent) {
  return new CuteQAbstractItemDelegate(parent);
}

//  QAbstractItemDelegate::~QAbstractItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractItemDelegateD1Ev(QAbstractItemDelegate *self) {
  delete self;
}

//  void QAbstractItemDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QAbstractItemDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->destroyEditor(editor, *index);
}

//  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QAbstractItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  bool QAbstractItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->editorEvent(event, model, *option, *index);
}

//  bool QAbstractItemDelegate::handleEditorEvent(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate17handleEditorEventEP7QObjectP6QEvent(
    QAbstractItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return self->handleEditorEvent(object, event);
}

//  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
//      QAbstractItemView *view, const QStyleOptionViewItem &option, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QHelpEvent *event,
    QAbstractItemView *view,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->helpEvent(event, view, *option, *index);
}

//  QList<int> QAbstractItemDelegate::paintingRoles() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK21QAbstractItemDelegate13paintingRolesEv(
    const QAbstractItemDelegate *self) {
  return new QList<int>(self->paintingRoles());
}

//  void QAbstractItemDelegate::commitData(QWidget *editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractItemDelegate10commitDataEP7QWidget(
    QAbstractItemDelegate *self,
    QWidget *editor) {
  self->commitData(editor);
}

//  void QAbstractItemDelegate::closeEditor(QWidget *editor,
//      QAbstractItemDelegate::EndEditHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractItemDelegate11closeEditorEP7QWidgetNS_11EndEditHintE(
    QAbstractItemDelegate *self,
    QWidget *editor,
    QAbstractItemDelegate::EndEditHint hint) {
  self->closeEditor(editor, hint);
}

//  void QAbstractItemDelegate::sizeHintChanged(const QModelIndex &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractItemDelegate15sizeHintChangedERK11QModelIndex(
    QAbstractItemDelegate *self,
    const QModelIndex *a0) {
  self->sizeHintChanged(*a0);
}

//  QAbstractItemDelegate::QAbstractItemDelegate(QObjectPrivate &a0, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZN21QAbstractItemDelegateC1ER14QObjectPrivateP7QObject(
    QObjectPrivate *a0,
    QObject *parent) {
  return new CuteQAbstractItemDelegate(*a0, parent);
}

//  QAbstractItemDelegatePrivate *QAbstractItemDelegate::d_func()
extern "C" Q_DECL_EXPORT
QAbstractItemDelegatePrivate *ritual_ZN21QAbstractItemDelegate6d_funcEv(
    QAbstractItemDelegate *self) {
  return self->d_func();
}

//  const QAbstractItemDelegatePrivate *QAbstractItemDelegate::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemDelegatePrivate *ritual_ZNK21QAbstractItemDelegate6d_funcEv(
    const QAbstractItemDelegate *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractItemDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemDelegate(
    QAbstractItemDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemDelegate *>(self)->take(key, call);
}

//  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->QAbstractItemDelegate::createEditor(parent, *option, *index);
}

//  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->QAbstractItemDelegate::destroyEditor(editor, *index);
}

//  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->QAbstractItemDelegate::setEditorData(editor, *index);
}

//  void QAbstractItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->QAbstractItemDelegate::setModelData(editor, model, *index);
}

//  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->QAbstractItemDelegate::updateEditorGeometry(editor, *option, *index);
}

//  bool QAbstractItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->QAbstractItemDelegate::editorEvent(
      event,
      model,
      *option,
      *index);
}

//  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
//      QAbstractItemView *view, const QStyleOptionViewItem &option, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QHelpEvent *event,
    QAbstractItemView *view,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->QAbstractItemDelegate::helpEvent(
      event,
      view,
      *option,
      *index);
}

//  a QList<int> a ritual of QAbstractItemDelegate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemDelegate__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
