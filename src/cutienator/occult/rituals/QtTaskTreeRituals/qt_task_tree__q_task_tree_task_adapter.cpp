//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  void QtTaskTree::QTaskTreeTaskAdapter::operator()(QTaskTree *task,
//      QTaskInterface *iface) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QtTaskTree20QTaskTreeTaskAdapterclEPNS_9QTaskTreeEPNS_14QTaskInterfaceE(
    const QtTaskTree::QTaskTreeTaskAdapter *self,
    QtTaskTree::QTaskTree *task,
    QtTaskTree::QTaskInterface *iface) {
  self->operator()(task, iface);
}

//  QtTaskTree::QTaskTreeTaskAdapter::~QTaskTreeTaskAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree20QTaskTreeTaskAdapterD1Ev(
    QtTaskTree::QTaskTreeTaskAdapter *self) {
  delete self;
}
