//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, rituals for functions the generator leaves out: 3. Kept as
//  it is when the generator runs again.
#include <QtCore/qlatin1stringmatcher.h>

//  QtPrivate::QCaseInsensitiveLatin1Hash::QCaseInsensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
QtPrivate::QCaseInsensitiveLatin1Hash *ritual_ZN9QtPrivate26QCaseInsensitiveLatin1HashC1Ev() {
  return new QtPrivate::QCaseInsensitiveLatin1Hash();
}

//  std::size_t QtPrivate::QCaseInsensitiveLatin1Hash::operator()(char c)
//      const
extern "C" Q_DECL_EXPORT
std::size_t ritual_ZNK9QtPrivate26QCaseInsensitiveLatin1HashclEc(
    const QtPrivate::QCaseInsensitiveLatin1Hash *self,
    char c) {
  return self->operator()(c);
}

//  int QtPrivate::QCaseInsensitiveLatin1Hash::difference(char lhs, char rhs)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate26QCaseInsensitiveLatin1Hash10differenceEcc(
    char lhs,
    char rhs) {
  return QtPrivate::QCaseInsensitiveLatin1Hash::difference(lhs, rhs);
}

//  QtPrivate::QCaseInsensitiveLatin1Hash::~QCaseInsensitiveLatin1Hash()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate26QCaseInsensitiveLatin1HashD1Ev(
    QtPrivate::QCaseInsensitiveLatin1Hash *self) {
  delete self;
}

//  static auto QtPrivate::QCaseInsensitiveLatin1Hash::matcher(char ch)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtPrivate26QCaseInsensitiveLatin1Hash7matcherEc(
    char ch) {
  return new auto(QtPrivate::QCaseInsensitiveLatin1Hash::matcher(ch));
}

//  bool (lambda of
//      QtPrivate::QCaseInsensitiveLatin1Hash::matcher)::operator()(char
//      other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZZN9QtPrivate26QCaseInsensitiveLatin1Hash7matcherEcENKUlcE_clEc(
    const void *self,
    char other) {
  using Matcher = decltype(QtPrivate::QCaseInsensitiveLatin1Hash::matcher('\0'));
  return (*static_cast<const Matcher *>(self))(other);
}

//  a lambda QtPrivate::QCaseInsensitiveLatin1Hash::matcher gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtPrivate_QCaseInsensitiveLatin1Hash__matcher(
    void *self) {
  using Matcher = decltype(QtPrivate::QCaseInsensitiveLatin1Hash::matcher('\0'));
  delete static_cast<Matcher *>(self);
}
