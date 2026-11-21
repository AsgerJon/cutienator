//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrunnable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrunnable.h>

//  void QRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnable3runEv(QRunnable *self) {
  self->run();
}

//  QRunnable::~QRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnableD1Ev(QRunnable *self) {
  delete self;
}

//  bool QRunnable::autoDelete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRunnable10autoDeleteEv(const QRunnable *self) {
  return self->autoDelete();
}

//  void QRunnable::setAutoDelete(bool autoDelete)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnable13setAutoDeleteEb(QRunnable *self, bool autoDelete) {
  self->setAutoDelete(autoDelete);
}
