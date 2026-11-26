//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::QTimeoutTaskAdapter::QTimeoutTaskAdapter()
extern "C" Q_DECL_EXPORT
QtTaskTree::QTimeoutTaskAdapter *ritual_ZN10QtTaskTree19QTimeoutTaskAdapterC1Ev() {
  return new QtTaskTree::QTimeoutTaskAdapter();
}

//  QtTaskTree::QTimeoutTaskAdapter::~QTimeoutTaskAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QTimeoutTaskAdapterD1Ev(
    QtTaskTree::QTimeoutTaskAdapter *self) {
  delete self;
}

//  void
//      QtTaskTree::QTimeoutTaskAdapter::operator()(std::chrono::milliseconds
//      *task, QTaskInterface *iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree19QTimeoutTaskAdapterclEPNSt6chrono8durationIlSt5ratioILl1ELl1000EEEEPNS_14QTaskInterfaceE(
    QtTaskTree::QTimeoutTaskAdapter *self,
    std::chrono::milliseconds *task,
    QtTaskTree::QTaskInterface *iface) {
  self->operator()(task, iface);
}
