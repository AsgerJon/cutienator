//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/6.12.0/QtPdf/private/qpdffile_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPdf/6.12.0/QtPdf/private/qtpdfglobal_p.h>
#include <QtPdf/QtPdf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdf/6.12.0/QtPdf/private/qpdffile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QPdfFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QPdfFile10metaObjectEv(const QPdfFile *self) {
  return self->metaObject();
}

//  void *QPdfFile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QPdfFile11qt_metacastEPKc(QPdfFile *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfFile::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QPdfFile11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfFile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QPdfFile2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QPdfFile::tr(s, c, n));
}

//  QPdfFile::QPdfFile(QPdfDocument *doc)
extern "C" Q_DECL_EXPORT
QPdfFile *ritual_ZN8QPdfFileC1EP12QPdfDocument(QPdfDocument *doc) {
  return new QPdfFile(doc);
}

//  QPdfDocument *QPdfFile::document()
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZN8QPdfFile8documentEv(QPdfFile *self) {
  return self->document();
}
