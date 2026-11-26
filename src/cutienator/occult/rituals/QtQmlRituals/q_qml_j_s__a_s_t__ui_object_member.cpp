//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Not written: the constructor, as a node is made in a
//  QQmlJS::MemoryPool (the 'operator new' of Managed takes only that).
//  'firstSourceLocation' and 'lastSourceLocation' are pure here, so
//  they have no 'own' ritual, and their Cute functions give an empty
//  SourceLocation when Python has taken nothing over for them.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <cstring>

//  A QQmlJS::AST::UiObjectMember that Python can take functions over
//  in. Every QQmlJS::AST::UiObjectMember Python makes is one. Each
//  function below asks the Python function handed over for it, and runs
//  Qt's own without one.
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_UiObjectMemberCall0)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_UiObjectMemberCall1)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_UiObjectMemberCall2)(const void *, int *);
class CuteQQmlJS_AST_UiObjectMember : public QQmlJS::AST::UiObjectMember {
public:
  using QQmlJS::AST::UiObjectMember::UiObjectMember;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST14UiObjectMember19firstSourceLocationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST14UiObjectMember18lastSourceLocationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14UiObjectMember18uiObjectMemberCastEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  SourceLocation QQmlJS::AST::UiObjectMember::firstSourceLocation()
  //      const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_UiObjectMemberCall0 call = reinterpret_cast<CuteQQmlJS_AST_UiObjectMemberCall0>(taken[0]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::SourceLocation();
  }

  //  SourceLocation QQmlJS::AST::UiObjectMember::lastSourceLocation()
  //      const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_UiObjectMemberCall1 call = reinterpret_cast<CuteQQmlJS_AST_UiObjectMemberCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::SourceLocation();
  }

  //  UiObjectMember *QQmlJS::AST::UiObjectMember::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_UiObjectMemberCall2 call = reinterpret_cast<CuteQQmlJS_AST_UiObjectMemberCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::UiObjectMember::uiObjectMemberCast();
  }
};

//  SourceLocation QQmlJS::AST::UiObjectMember::firstSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiObjectMember19firstSourceLocationEv(
    const QQmlJS::AST::UiObjectMember *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::UiObjectMember::lastSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14UiObjectMember18lastSourceLocationEv(
    const QQmlJS::AST::UiObjectMember *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  UiObjectMember *QQmlJS::AST::UiObjectMember::uiObjectMemberCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiObjectMember *ritual_ZN6QQmlJS3AST14UiObjectMember18uiObjectMemberCastEv(
    QQmlJS::AST::UiObjectMember *self) {
  return self->uiObjectMemberCast();
}

//  a Python function taken by a CuteQQmlJS_AST_UiObjectMember, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_UiObjectMember(
    QQmlJS::AST::UiObjectMember *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_UiObjectMember *>(self)->take(key, call);
}

//  UiObjectMember *QQmlJS::AST::UiObjectMember::uiObjectMemberCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiObjectMember *ritual_own_ZN6QQmlJS3AST14UiObjectMember18uiObjectMemberCastEv(
    QQmlJS::AST::UiObjectMember *self) {
  return self->QQmlJS::AST::UiObjectMember::uiObjectMemberCast();
}
