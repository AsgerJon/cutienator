//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qcapturablewindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qcapturablewindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QCapturableWindow::QCapturableWindow()
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowC1Ev() {
  return new QCapturableWindow();
}

//  QCapturableWindow::QCapturableWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowC1EP7QWindow(
    QWindow *window) {
  return new QCapturableWindow(window);
}

//  QCapturableWindow::~QCapturableWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCapturableWindowD1Ev(QCapturableWindow *self) {
  delete self;
}

//  QCapturableWindow::QCapturableWindow(const QCapturableWindow &other)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowC1ERKS_(
    const QCapturableWindow *other) {
  return new QCapturableWindow(*other);
}

//  QCapturableWindow::QCapturableWindow(QCapturableWindow &&other)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowC1EOS_(
    QCapturableWindow *other) {
  return new QCapturableWindow(std::move(*other));
}

//  QCapturableWindow &QCapturableWindow::operator=(const QCapturableWindow
//      &other)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowaSERKS_(
    QCapturableWindow *self,
    const QCapturableWindow *other) {
  return &(self->operator=(*other));
}

//  QCapturableWindow &QCapturableWindow::operator=(QCapturableWindow
//      &&other)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowaSEOS_(
    QCapturableWindow *self,
    QCapturableWindow *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCapturableWindow::swap(QCapturableWindow &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCapturableWindow4swapERS_(
    QCapturableWindow *self,
    QCapturableWindow *other) {
  self->swap(*other);
}

//  bool operator==(const QCapturableWindow &lhs, const QCapturableWindow
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QCapturableWindowS1_(
    const QCapturableWindow *lhs,
    const QCapturableWindow *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCapturableWindow &lhs, const QCapturableWindow
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QCapturableWindowS1_(
    const QCapturableWindow *lhs,
    const QCapturableWindow *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QCapturableWindow::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCapturableWindow7isValidEv(const QCapturableWindow *self) {
  return self->isValid();
}

//  QString QCapturableWindow::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCapturableWindow11descriptionEv(
    const QCapturableWindow *self) {
  return new QString(self->description());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCapturableWindow &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK17QCapturableWindow(
    const QDebug *a0,
    const QCapturableWindow *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QCapturableWindow::QCapturableWindow(QCapturableWindowPrivate
//      *capturablePrivate)
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZN17QCapturableWindowC1EP24QCapturableWindowPrivate(
    QCapturableWindowPrivate *capturablePrivate) {
  return new QCapturableWindow(capturablePrivate);
}

//  QList<QCapturableWindow>::QList()
extern "C" Q_DECL_EXPORT
QList<QCapturableWindow> *ritual_list_make_QCapturableWindow() {
  return new QList<QCapturableWindow>();
}

//  void QList<QCapturableWindow>::append(const QCapturableWindow &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCapturableWindow(
    QList<QCapturableWindow> *self,
    const QCapturableWindow *element) {
  self->append(*element);
}

//  qsizetype QList<QCapturableWindow>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCapturableWindow(
    const QList<QCapturableWindow> *self) {
  return self->size();
}

//  const QCapturableWindow &QList<QCapturableWindow>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_list_at_QCapturableWindow(
    const QList<QCapturableWindow> *self,
    long long index) {
  return new QCapturableWindow(self->at(index));
}

//  QList<QCapturableWindow>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCapturableWindow(QList<QCapturableWindow> *self) {
  delete self;
}
