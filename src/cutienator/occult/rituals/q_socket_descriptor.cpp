//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsocketnotifier.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsocketnotifier.h>

//  QSocketDescriptor::QSocketDescriptor(DescriptorType descriptor)
extern "C" Q_DECL_EXPORT
QSocketDescriptor *ritual_ZN17QSocketDescriptorC1Ei(
    QSocketDescriptor::DescriptorType descriptor) {
  return new QSocketDescriptor(descriptor);
}

//  DescriptorType QSocketDescriptor::operator int() const
extern "C" Q_DECL_EXPORT
QSocketDescriptor::DescriptorType ritual_ZNK17QSocketDescriptorcviEv(
    const QSocketDescriptor *self) {
  return self->operator QSocketDescriptor::DescriptorType();
}

//  bool QSocketDescriptor::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSocketDescriptor7isValidEv(const QSocketDescriptor *self) {
  return self->isValid();
}

//  QSocketDescriptor::~QSocketDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSocketDescriptorD1Ev(QSocketDescriptor *self) {
  delete self;
}
