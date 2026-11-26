//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>
#include <QtCore/qstring.h>

//  Group QtTaskTree::ExecutableItem::withTimeout(std::chrono::milliseconds
//      timeout, const std::function<void ()> &handler) const
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZNK10QtTaskTree14ExecutableItem11withTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEERKSt8functionIFvvEE(
    const QtTaskTree::ExecutableItem *self,
    long long timeout,
    const std::function<void ()> *handler) {
  return new QtTaskTree::Group(
      self->withTimeout(
          std::chrono::milliseconds(timeout),
          *handler));
}

//  Group QtTaskTree::ExecutableItem::withLog(const QString &logName) const
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZNK10QtTaskTree14ExecutableItem7withLogERK7QString(
    const QtTaskTree::ExecutableItem *self,
    const QString *logName) {
  return new QtTaskTree::Group(self->withLog(*logName));
}

//  QtTaskTree::ExecutableItem::ExecutableItem()
extern "C" Q_DECL_EXPORT
QtTaskTree::ExecutableItem *ritual_ZN10QtTaskTree14ExecutableItemC1Ev() {
  return new QtTaskTree::ExecutableItem();
}

//  QtTaskTree::ExecutableItem::ExecutableItem(const TaskHandler &handler)
extern "C" Q_DECL_EXPORT
QtTaskTree::ExecutableItem *ritual_ZN10QtTaskTree14ExecutableItemC1ERKNS_9GroupItem11TaskHandlerE(
    const QtTaskTree::GroupItem::TaskHandler *handler) {
  return new QtTaskTree::ExecutableItem(*handler);
}

//  Group operator!(const ExecutableItem &item)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreentERKNS_14ExecutableItemE(
    const QtTaskTree::ExecutableItem *item) {
  return new QtTaskTree::Group(operator!(*item));
}

//  Group operator&&(const ExecutableItem &first, const ExecutableItem
//      &second)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeaaERKNS_14ExecutableItemES2_(
    const QtTaskTree::ExecutableItem *first,
    const QtTaskTree::ExecutableItem *second) {
  return new QtTaskTree::Group(operator&&(*first, *second));
}

//  Group operator||(const ExecutableItem &first, const ExecutableItem
//      &second)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeooERKNS_14ExecutableItemES2_(
    const QtTaskTree::ExecutableItem *first,
    const QtTaskTree::ExecutableItem *second) {
  return new QtTaskTree::Group(operator||(*first, *second));
}

//  Group operator&&(const ExecutableItem &item, DoneResult result)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeaaERKNS_14ExecutableItemENS_10DoneResultE(
    const QtTaskTree::ExecutableItem *item,
    QtTaskTree::DoneResult result) {
  return new QtTaskTree::Group(operator&&(*item, result));
}

//  Group operator||(const ExecutableItem &item, DoneResult result)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeooERKNS_14ExecutableItemENS_10DoneResultE(
    const QtTaskTree::ExecutableItem *item,
    QtTaskTree::DoneResult result) {
  return new QtTaskTree::Group(operator||(*item, result));
}

//  Group QtTaskTree::ExecutableItem::withCancelImpl(const ConnectWrapper
//      &connectWrapper, const GroupItems &postCancelRecipe) const
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZNK10QtTaskTree14ExecutableItem14withCancelImplERKSt8functionIFvP7QObjectRKS1_IFvvEEEERK5QListINS_9GroupItemEE(
    const QtTaskTree::ExecutableItem *self,
    const QtTaskTree::ExecutableItem::ConnectWrapper *connectWrapper,
    const QtTaskTree::GroupItems *postCancelRecipe) {
  return new QtTaskTree::Group(
      self->withCancelImpl(
          *connectWrapper,
          *postCancelRecipe));
}

//  Group QtTaskTree::ExecutableItem::withAcceptImpl(const ConnectWrapper
//      &connectWrapper) const
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZNK10QtTaskTree14ExecutableItem14withAcceptImplERKSt8functionIFvP7QObjectRKS1_IFvvEEEE(
    const QtTaskTree::ExecutableItem *self,
    const QtTaskTree::ExecutableItem::ConnectWrapper *connectWrapper) {
  return new QtTaskTree::Group(self->withAcceptImpl(*connectWrapper));
}

//  QtTaskTree::ExecutableItem::~ExecutableItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree14ExecutableItemD1Ev(
    QtTaskTree::ExecutableItem *self) {
  delete self;
}
