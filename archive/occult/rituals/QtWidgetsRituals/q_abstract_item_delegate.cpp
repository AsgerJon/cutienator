//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractitemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractItemDelegate that Python can take functions over in. Every QAbstractItemDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractItemDelegateCall0)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef const QSize * (*CuteQAbstractItemDelegateCall1)(const void *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void * (*CuteQAbstractItemDelegateCall2)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void (*CuteQAbstractItemDelegateCall3)(const void *, QWidget *, const QModelIndex *, int *);
typedef void (*CuteQAbstractItemDelegateCall4)(const void *, QWidget *, const QModelIndex *, int *);
typedef void (*CuteQAbstractItemDelegateCall5)(const void *, QWidget *, QAbstractItemModel *, const QModelIndex *, int *);
typedef void (*CuteQAbstractItemDelegateCall6)(const void *, QWidget *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractItemDelegateCall7)(const void *, QEvent *, QAbstractItemModel *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractItemDelegateCall8)(const void *, QHelpEvent *, QAbstractItemView *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractItemDelegateCall9)(const void *, QEvent *, int *);
typedef bool (*CuteQAbstractItemDelegateCall10)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAbstractItemDelegateCall11)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAbstractItemDelegateCall12)(const void *, QChildEvent *, int *);
typedef void (*CuteQAbstractItemDelegateCall13)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractItemDelegateCall14)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAbstractItemDelegateCall15)(const void *, const QMetaMethod *, int *);
class CuteQAbstractItemDelegate : public QAbstractItemDelegate {
public:
  using QAbstractItemDelegate::QAbstractItemDelegate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
    return false;
  }

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
};

//  const QMetaObject *QAbstractItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractItemDelegate10metaObjectEv(
    const QAbstractItemDelegate *self) {
  return self->metaObject();
}

//  QString QAbstractItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemDelegate::tr(s, c, n));
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
